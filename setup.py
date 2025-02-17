from pathlib import Path
from setuptools import find_namespace_packages, setup

# Define paths
ROOT_DIR = Path(__file__).parent
DOCS_PATH = ROOT_DIR / "docs" / "README.md"
README_PATH = ROOT_DIR / "README.md"
VERSION_PATH = ROOT_DIR / "src" / "shaluai" / "version.py"

# Ensure README.md exists by copying from docs/
if DOCS_PATH.exists() and not README_PATH.exists():
    README_PATH.write_text(DOCS_PATH.read_text(encoding="utf-8"), encoding="utf-8")

# Extract version from version.py, fallback to "1.0.0" if missing
if VERSION_PATH.exists():
    version = VERSION_PATH.read_text(encoding="utf-8").split('"')[1]
else:
    version = "1.0.0"

# Read long description safely
long_description = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else "ShaluAI – The Ultimate Autonomous AI Assistant"

# Setup configuration
setup(
    name="shaluai",
    version=version,
    description="ShaluAI – The Ultimate Autonomous AI Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PrathamPrasad148/ShaluAI",
    project_urls={
        "Bug Report": "https://github.com/PrathamPrasad148/ShaluAI/issues/new?labels=bug-report",
        "Feature Request": "https://github.com/PrathamPrasad148/ShaluAI/issues/new?labels=enhancement",
    },
    author="Pratham Prasad",
    author_email="prathamprasad@example.com",
    license="GNU General Public License v3.0",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["shaluai"],
    package_data={"": ["*.json"]},
    install_requires=[
        "requests[socks]",
        "httpx[socks]",
        "prompt-toolkit",
        "tiktoken>=0.3.0",
        "openai",
        "rich",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: AI Researchers",
        "Topic :: Software Development :: Artificial Intelligence",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
