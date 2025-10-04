from pathlib import Path
import setuptools
from setuptools.command.build import build
import subprocess
import os
import tomllib


class CustomBuild(build):
    """
    Custom build that ensures the frontend assets are built before the Python package is built.

    The GH workflow we use for publishing python packages requires using `poetry build` to build the package.
    So we customize the build steps here to include building the frontend code so it can be included
    in the python package
    """

    def run(self):
        print("Custom build command running...")
        self.build_frontend()
        build.run(self)

    def build_frontend(self):
        """Build frontend assets, but skip if dist artifacts already exist (e.g., from sdist).

        In CI (source tree), we build via Yarn. In PEP 517 wheel-from-sdist builds, the dist
        directories are already present; we should not re-run JS builds there.
        """
        cwd = Path(__file__).parent.joinpath("streamlit_tetrascience_ui/components")
        packages_dir = cwd / "packages"
        dist_paths = [
            packages_dir / "streamlit-component-lib" / "dist",
            packages_dir / "ui" / "dist",
            packages_dir / "frontend" / "dist",
        ]
        # If all required dist directories exist and are non-empty, skip rebuilding
        if all(p.exists() and any(p.rglob("*")) for p in dist_paths):
            print("Frontend dist assets already present; skipping build.")
            return

        # Otherwise, perform per-package builds
        build_order = ["streamlit-component-lib", "ui", "frontend"]
        if cwd.joinpath("package.json").exists():
            subprocess.run(["bash", "-lc", "yarn install"], check=True, cwd=cwd)
        for name in build_order:
            pkg_path = packages_dir / name
            if pkg_path.exists() and pkg_path.joinpath("package.json").exists():
                subprocess.run(
                    ["bash", "-lc", f"yarn --cwd {pkg_path} install"],
                    check=True,
                    cwd=cwd,
                )
                subprocess.run(
                    ["bash", "-lc", f"yarn --cwd {pkg_path} run build"],
                    check=True,
                    cwd=cwd,
                )
        print("Frontend assets built (per-package builds).")


with open("README.md", "r") as fh:
    long_description = fh.read()

version_from_env = os.environ.get("TSPKG_VERSION", "0.2.0")


# Derive install_requires and python_requires from pyproject.toml [tool.poetry.dependencies]
# so we keep a single source of truth (Poetry) while building with setuptools.
def _convert_poetry_spec(spec: str) -> str:
    spec = (spec or "").strip()
    if not spec:
        return spec
    # Convert Poetry caret (^) to a PEP 440-compatible range
    if spec.startswith("^"):
        ver = spec[1:].strip()
        parts = (ver + ".0.0").split(".")[:3]
        try:
            major, minor, patch = map(int, parts)
        except Exception:
            return ver  # fallback
        if major > 0:
            upper = f"{major + 1}.0.0"
        else:
            # ^0.x.y -> <0.(x+1).0 per caret semantics
            upper = f"0.{minor + 1}.0"
        return f">={ver},<{upper}"
    # If spec looks like a bare version (e.g., 1.2.3), turn into exact pin
    if spec[0].isdigit():
        return f"=={spec}"
    return spec


def _read_poetry_requirements(pyproject_path: str = "pyproject.toml"):
    if tomllib is None:
        return None, []
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    deps = data.get("tool", {}).get("poetry", {}).get("dependencies", {})
    python_req = None
    reqs = []
    for name, value in deps.items():
        if name == "python":
            python_req = str(value)
            continue
        extras = ""
        spec = ""
        if isinstance(value, str):
            spec = _convert_poetry_spec(value)
        elif isinstance(value, dict):
            if value.get("extras"):
                extras = "[" + ",".join(value["extras"]) + "]"
            if value.get("version"):
                spec = _convert_poetry_spec(str(value["version"]))
        # Normalize to no spaces: pkg[extra]>=x,<y
        if spec:
            # Ensure spec starts with an operator for exact versions
            if spec[0].isdigit():
                spec = "==" + spec
            entry = f"{name}{extras}{spec}"
        else:
            entry = name
        reqs.append(entry)
    return python_req, reqs


python_req, install_reqs = _read_poetry_requirements()
if not install_reqs:
    # Fallback minimal list if tomllib is not available (should not happen)
    install_reqs = [
        "streamlit>=0.63",
        "ts-sdk-connectors-python>=2.0.0",
        "pyjwt>=2.8.0",
    ]

setuptools.setup(
    name="tetrascience-streamlit-ui",
    version=version_from_env,
    author="TetraScience",
    description="Use Tetrascience UI components in Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tetrascience/ts-lib-ui-kit-streamlit",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=python_req or ">=3.11",
    install_requires=install_reqs,
    cmdclass={
        "build": CustomBuild,
    },
)
