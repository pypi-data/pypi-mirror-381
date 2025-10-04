# tetrascience-streamlit-ui

TetraScience UI components and data app providers for [Streamlit](https://streamlit.io/).

This library provides:

- **UI Components**: Reusable Streamlit components for TetraScience applications
- **Data App Providers**: SDK functions for retrieving different provider types from the TetraScience platform

## Installation

To install and set up the TetraScience UI components for Streamlit, follow these steps:

1. **Install prerequisites:**

   - Python 3.11+
   - Node.js (v20+ recommended)
   - [yarn 4](https://yarnpkg.com/)
   - [Poetry](https://python-poetry.org/docs/#installation)

2. **Install the package**

```
poetry add tetrascience-streamlit-ui
```

## Usage

### UI Components

```python
from tetrascience.ui.histogram import histogram
from tetrascience.ui.code_editor import code_editor
from tetrascience.ui.protocol_yaml_card import protocol_yaml_card

# Example: Histogram component
dist_result = histogram(name="Sample Distribution", key="hist1")

# Example: Code Editor
code = code_editor(value="# Python code here", language="python", height="200px", key="code1")

# Example: Protocol YAML Card
protocol_yaml_card(
    title="Protocol Editor",
    version_options=[
        {"label": "v1.0.0", "value": "v1.0.0"},
        {"label": "v0.9.2", "value": "v0.9.2"},
    ],
    selected_version="v1.0.0",
    yaml="# Example YAML\nname: Protocol",
    key="protocol1"
)
```

## Data App Providers

The `data_app_providers` module provides functionality for retrieving and using database provider configurations from the TetraScience Data Platform (TDP). This is useful for data apps that need to connect to various databases like Snowflake, Databricks, or Athena.

### Basic Usage

```python
from tetrascience.data_app_providers import (
    get_provider_configurations,
    build_provider,
    TetraScienceClient,
)

# Create TDP client
client = TetraScienceClient(
    token="your-auth-token",
    x_org_slug="your-org-slug",
    base_url="https://api.tetrascience.com"
)

# Get provider configurations from TDP
configs = get_provider_configurations(client)

# Build and use a provider
for config in configs:
    provider = build_provider(config)
    df = provider.query("SELECT * FROM my_table LIMIT 10")
    print(df.head())
```

### Environment Variable Configuration (Development)

For local development, you can specify provider configurations directly via environment variable:

```python
import os
import json
from tetrascience.data_app_providers import get_provider_configurations, build_provider

# Set provider configuration
provider_config = [
    {
        "name": "Dev Snowflake",
        "type": "snowflake",
        "iconUrl": "https://example.com/snowflake.png",
        "fields": {
            "user": "dev_user",
            "password": "dev_password",
            "account": "dev.snowflakecomputing.com",
            "warehouse": "DEV_WH",
            "database": "DEV_DB",
            "schema": "PUBLIC",
            "role": "DEV_ROLE"
        }
    }
]

os.environ["DATA_APP_PROVIDER_CONFIG"] = json.dumps(provider_config)

# Get configurations (client still needed but won't be used for env var mode)
client = TetraScienceClient()  # Can be empty for env var mode
configs = get_provider_configurations(client)
provider = build_provider(configs[0])
```

### Production Usage (TDP Integration)

In production data apps, provider configurations are retrieved from TDP using a connector ID:

```python
# Environment variables set by data app runtime:
# CONNECTOR_ID=your-connector-id
# ORG_SLUG=your-org-slug
# TDP_ENDPOINT=https://api.tetrascience.com

# Provider secrets also set by environment:
# SNOWFLAKE_USER=actual_user
# SNOWFLAKE_PASSWORD=actual_password
# DATABRICKS_CLIENT_ID=actual_client_id
# etc.

from tetrascience.data_app_providers import (
    get_provider_configurations,
    build_provider,
    TetraScienceClient,
)

client = TetraScienceClient(
    token=os.getenv("TS_AUTH_TOKEN"),
    x_org_slug=os.getenv("ORG_SLUG"),
    base_url=os.getenv("TDP_ENDPOINT") or os.getenv("TDP_INTERNAL_ENDPOINT")
)

# Fetch provider configurations from TDP
configs = get_provider_configurations(client)

# Use providers
for config in configs:
    print(f"Using provider: {config.name} ({config.type})")
    provider = build_provider(config)

    # Query data
    df = provider.query("SELECT COUNT(*) as row_count FROM my_table")
    print(f"Row count: {df['row_count'][0]}")
```

### Supported Provider Types

- **Snowflake**: `snowflake-connector-python` required
- **Databricks**: `databricks-sql-connector[pyarrow]` required
- **Athena**: `pyathena[arrow]` and `boto3` required
  - **Local Development**: Requires AWS credentials to be configured (see [AWS Credentials Setup](#aws-credentials-for-athena-local-development) below)
  - **TDP Deployment**: AWS credentials are automatically configured for the Data App

### Provider Configuration Format

```python
{
    "name": "Human-readable provider name",
    "type": "snowflake|databricks|athena",
    "iconUrl": "https://example.com/icon.png",
    "fields": {
        # Provider-specific connection fields
        # Snowflake: user, password, account, warehouse, database, schema, role
        # Databricks: server_hostname, http_path, client_id, client_secret, catalog, schema
        # Athena: Uses AWS credentials and environment variables
    }
}
```

### Error Handling

```python
from tetrascience.data_app_providers.exceptions import (
    InvalidProviderConfigurationError,
    ConnectionError,
    QueryError,
    MissingTableError
)

try:
    configs = get_provider_configurations(client)
    provider = build_provider(configs[0])
    df = provider.query("SELECT * FROM non_existent_table")
except InvalidProviderConfigurationError as e:
    print(f"Configuration error: {e}")
except ConnectionError as e:
    print(f"Connection failed: {e}")
except MissingTableError as e:
    print(f"Table not found: {e}")
except QueryError as e:
    print(f"Query failed: {e}")
```

### AWS Credentials for Athena (Local Development)

When using the Athena provider for local development, you need to configure AWS credentials since the provider uses `boto3` to connect to AWS Athena. The Athena provider automatically uses the default TDP Athena configuration but requires valid AWS credentials.

#### Required Environment Variables

The following environment variables are used by the Athena provider:

```bash
# Required for Athena connection
AWS_REGION=us-east-1                    # Your AWS region
ATHENA_S3_OUTPUT_LOCATION=your-bucket   # S3 bucket for query results
ORG_SLUG=your-org-slug                  # Your organization slug
```

#### AWS Credentials Setup

Choose one of the following methods to configure AWS credentials for local development:

#### Option 1: AWS Credentials File

```bash
# Configure AWS credentials using AWS CLI
aws configure

# Or manually create ~/.aws/credentials
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

#### Option 2: Environment Variables

```bash
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
```

#### TDP Deployment vs Local Development

- **Local Development**: You must manually configure AWS credentials using one of the methods above
- **TDP Deployment**: AWS credentials are automatically provided by the connector runtime environment

#### Example: Local Athena Development

```python
import os
import json
from tetrascience.data_app_providers import get_provider_configurations, build_provider, TetraScienceClient

# Set required environment variables for local development
os.environ["AWS_REGION"] = "us-east-1"
os.environ["ATHENA_S3_OUTPUT_LOCATION"] = "your-athena-results-bucket"
os.environ["ORG_SLUG"] = "your-org-slug"

# Configure Athena provider via environment variable
athena_config = [{
    "name": "Local Athena",
    "type": "athena",
    "iconUrl": "https://example.com/athena.png",
    "fields": {}  # Athena uses AWS credentials and environment variables
}]

os.environ["DATA_APP_PROVIDER_CONFIG"] = json.dumps(athena_config)

# Build and use Athena provider
client = TetraScienceClient()  # Empty client for env var mode
configs = get_provider_configurations(client)
athena_provider = build_provider(configs[0])

# Query data (requires valid AWS credentials)
df = athena_provider.query("SELECT COUNT(*) as total FROM your_table")
print(f"Total rows: {df['total'][0]}")
```

## JWT Token Manager (Data Apps Authentication)

The `JWTTokenManager` helps your data app obtain a valid JWT to call the TetraScience Data Platform (TDP) APIs. It supports both:

- Using a standard `ts-auth-token` JWT (from cookie or `TS_AUTH_TOKEN` env var)
- Resolving a `ts-token-ref` cookie into a full JWT via the connector key-value store

### When to use it

Use this in your Streamlit data apps to:

- Read the user's auth token from cookies when deployed on TDP
- Fall back to a local `TS_AUTH_TOKEN` during development

### Environment variables

- `CONNECTOR_ID` (required for ts-token-ref flow)
- `ORG_SLUG` (organization slug)
- `TDP_ENDPOINT` or `TDP_INTERNAL_ENDPOINT` (API base URL; picked automatically if set)
- `TS_AUTH_TOKEN` (optional for local dev; used if cookies are not available)

### Basic (local development) example

For local dev, set `TS_AUTH_TOKEN` and call `get_user_token` with an empty cookie dict. The manager will use the env var.

```python
import os
import streamlit as st
from tetrascience.data_apps.jwt_token_manager import jwt_manager

# export TS_AUTH_TOKEN=... and ORG_SLUG=...
org_slug = os.getenv("ORG_SLUG", "your-org")

# No cookies in local dev; falls back to TS_AUTH_TOKEN
jwt_token = jwt_manager.get_user_token(cookies={}, org_slug=org_slug)
if not jwt_token:
    st.warning('Failed to retrieve JWT token')

# Use the token to make authenticated requests to TDP
```

### Production (TDP) example using cookies

In TDP, your app runs behind a proxy that sets cookies. Use a cookie utility to read them (for example, `extra-streamlit-components`' CookieManager), then pass them to the manager.

```python
import os
import streamlit as st
from tetrascience.data_apps.jwt_token_manager import jwt_manager

org_slug = os.environ["ORG_SLUG"]

# Read cookies (contains ts-auth-token or ts-token-ref)
cookies = st.context.cookies.to_dict()

# Resolves the users JWT token. Either the `ts-auth-token` cookie, or resolves the `ts-token-ref` cookie into a full JWT.
jwt_token = jwt_manager.get_user_token(cookies=cookies, org_slug=org_slug)
if not jwt_token:
    st.warning('Failed to retrieve JWT token')

# Use the token to make authenticated requests to TDP
```

Notes:

- Tokens are cached and auto-refreshed when close to expiry.
- Errors are surfaced in Streamlit via `st.warning`/`st.error` to help with troubleshooting.

## Features

### UI Components (Summary)

- Custom Streamlit components for TetraScience UI
- Easy integration and usage
- Example components: `my_component`, `histogram`, `bar_graph`, `chromatogram`, `protocol_yaml_card`, `button`, `input`, `dropdown`, `checkbox`, `badge`, `label`, `textarea`, `code_editor`, `markdown_display`, `menu_item`, `tab`, `toast`, `toggle`, `tooltip`, and more.

### Data App Providers (Summary)

- Retrieve and manage data provider configurations from the TetraScience platform
- Connect to Snowflake, Databricks, and Athena databases
- Uses the standardized TetraScience SDK (`ts-sdk-connectors-python`) for TDP API interactions
- Configure providers via environment variables for local development

## License

Apache 2.0
