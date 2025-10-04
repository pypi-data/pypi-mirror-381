import os
from datetime import datetime, timedelta, timezone
from typing import Dict, Optional

import jwt
import streamlit as st
from ts_sdk_connectors_python.config import TdpApiConfig
from ts_sdk_connectors_python.constants import EnvVars
from ts_sdk_connectors_python.logger import get_logger
from ts_sdk_connectors_python.tdp_api_sync import TdpApiSync
from ts_sdk_connectors_python.utils import utc_time

logger = get_logger(__name__)

TDP_ENDPOINT = os.getenv("TDP_INTERNAL_ENDPOINT") or os.getenv(EnvVars.TDP_ENDPOINT)
JWT_TOKEN_PARAMETER_NAME = os.getenv(EnvVars.JWT_TOKEN_PARAMETER)
CONNECTOR_ID = os.getenv(EnvVars.CONNECTOR_ID)


class JWTTokenManager:
    """
    Manages JWT token retrieval and validation for ts-token-ref cookies.

    This class handles the resolution of ts-token-ref values (short references)
    into full JWT tokens by retrieving them from the connector's key-value store.
    User JWT tokens are cached with proper expiration handling to avoid
    unnecessary lookups.

    Token Flow:
    1. ts-token-ref (from cookie) → Full JWT token (from connector store)
    2. Full JWT token → Used for TDP API calls
    """

    def __init__(
        self,
        base_url: str = TDP_ENDPOINT,
    ):
        self.base_url = base_url
        self._token_cache = {}
        self.token_refresh_threshold = timedelta(minutes=5)
        self._tdp_api = None

    def _get_tdp_api(self, org_slug: str) -> Optional[TdpApiSync]:
        """
        Get or create a TdpApi instance for connector data operations.

        Returns:
            A TdpApi instance if successful, None otherwise
        """
        if self._tdp_api is not None:
            return self._tdp_api

        if not all([CONNECTOR_ID, self.base_url, org_slug]):
            logger.error(
                "Missing required configuration: CONNECTOR_ID, base_url, or org_slug"
            )
            return None

        try:
            # Create TdpApi instance for data operations
            config = TdpApiConfig(
                tdp_endpoint=self.base_url,
                connector_id=CONNECTOR_ID,
                org_slug=org_slug,
                artifact_type="data-app",
            )
            self._tdp_api = TdpApiSync(config)
            self._tdp_api.init_client()
            return self._tdp_api

        except Exception as e:
            logger.error(f"Failed to create TdpApi instance: {e}")
            return None

    def _decode_jwt_payload(self, token: str) -> Optional[Dict]:
        """
        Decode JWT payload

        Args:
            token: The JWT token to decode

        Returns:
            The JWT payload if successful, None otherwise
        """
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            return payload
        except jwt.InvalidTokenError as e:
            logger.warning(f"Invalid JWT token: {e}")
            return None
        except Exception as e:
            logger.error(f"Error decoding JWT: {e}")
            return None

    def _is_token_expiring_soon(self, token: str) -> bool:
        """
        Check if a JWT token is expiring within the refresh threshold (5 minutes).

        Args:
            token: The JWT token to check

        Returns:
            True if token is expiring soon or expired, False otherwise
        """
        payload = self._decode_jwt_payload(token)
        if not payload:
            return True

        exp = payload.get("exp")
        if not exp:
            logger.warning("JWT token has no expiration claim")
            return True

        try:
            expiry_time = datetime.fromtimestamp(exp, tz=timezone.utc)
            refresh_time = utc_time() + self.token_refresh_threshold

            is_expiring = expiry_time <= refresh_time
            if is_expiring:
                logger.debug(f"JWT token expiring at {expiry_time}, refreshing")

            return is_expiring

        except (ValueError, TypeError) as e:
            logger.error(f"Error parsing JWT expiration: {e}")
            return True

    def _get_valid_user_jwt(self, token_ref: str) -> Optional[str]:
        """
        Get a valid user JWT token.

        Returns:
            A valid user JWT token if available, None otherwise
        """
        cache_key = f"{token_ref}"
        cached_token = self._token_cache.get(cache_key)
        if cached_token and not self._is_token_expiring_soon(cached_token):
            return cached_token

        return None

    def get_jwt_from_token_ref(self, token_ref: str, org_slug: str) -> Optional[str]:
        """
        Retrieve the full JWT token using a ts-token-ref.

        Args:
            token_ref: The ts-token-ref value from the cookie
            org_slug: The organization slug

        Returns:
            The full JWT token if successful, None otherwise
        """
        if not all([token_ref, org_slug, self.base_url]):
            logger.warning("Missing required parameters for JWT token retrieval")
            return None

        # Check cache first
        cached_user_token = self._get_valid_user_jwt(token_ref)
        if cached_user_token:
            logger.debug("Returning cached user JWT token")
            return cached_user_token

        try:
            # Fetch the JWT token from the connector store
            return self._get_jwt_from_token_ref(token_ref, org_slug)
        except Exception as e:
            logger.error(f"Unexpected error while retrieving JWT token: {e}")
            return None

    def _get_jwt_from_token_ref(self, token_ref: str, org_slug: str) -> Optional[str]:
        """
        Retrieve JWT token from connector store.

        Args:
            token_ref: The ts-token-ref value from the cookie
            org_slug: The organization slug

        Returns:
            The full JWT token if successful, None otherwise
        """
        try:
            tdp_api = self._get_tdp_api(org_slug)
            if not tdp_api:
                logger.error("Failed to get TdpApi instance")
                return None

            # Get connector data from the K/V store
            response = tdp_api.get_connector_data(CONNECTOR_ID)

            if (
                response.status_code == 200
                and response.parsed
                and response.parsed.values
            ):
                # Find the token_ref in the response values
                found_item = next(
                    (item for item in response.parsed.values if item.key == token_ref),
                    None,
                )

                if found_item and found_item.value:
                    jwt_token = found_item.value["jwt"]
                    # Cache the token for future use
                    self._token_cache[token_ref] = jwt_token
                    logger.debug("Successfully retrieved JWT token from ts-token-ref")
                    return jwt_token
                else:
                    st.error(
                        f"JWT token not found for key '{token_ref}' in connector store"
                    )
            else:
                st.error(f"Failed to retrieve JWT token: HTTP {response.status_code}")

        except Exception as e:
            logger.error(f"Error retrieving JWT token: {e}")

        return None

    def get_user_token(self, cookies: Dict[str, str], org_slug: str) -> Optional[str]:
        """
        Get the best available token from cookies, handling both ts-auth-token and ts-token-ref.

        Args:
            cookies: Dictionary of cookies from the request
            org_slug: The organization slug

        Returns:
            The JWT token to use for API calls, None if none available
        """
        # Default to using the ts-auth-token if it is present
        auth_token = cookies.get("ts-auth-token") or os.getenv("TS_AUTH_TOKEN")
        if auth_token:
            logger.debug("Using standard ts-auth-token")
            return auth_token

        # If no auth token, try to resolve ts-token-ref
        token_ref = cookies.get("ts-token-ref")
        if token_ref:
            logger.debug("Found ts-token-ref, attempting to resolve to full JWT token")

            if CONNECTOR_ID:
                jwt_token = self.get_jwt_from_token_ref(token_ref, org_slug)
                if jwt_token:
                    return jwt_token
                else:
                    logger.warning("Failed to resolve ts-token-ref to JWT token")
            else:
                logger.error("Connector ID not configured")

        st.warning("No valid authentication token found")
        return None


# Global instance
jwt_manager = JWTTokenManager()
