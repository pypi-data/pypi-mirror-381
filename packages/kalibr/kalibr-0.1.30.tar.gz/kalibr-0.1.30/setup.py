from setuptools import setup, find_packages
import os

# Try to load README if it exists
long_desc = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        long_desc = f.read()

setup(
    name="kalibr",
    version="0.1.30",  # bump each release
    description="Kalibr SDK - Demo MCP/LLM integration layer",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Devon Kelley",
    author_email="devkelley@me.com",
    url="https://pypi.org/project/kalibr/",
    packages=find_packages(include=["kalibr", "kalibr.*"]),
    install_requires=[
        "fastapi>=0.118.0",
        "uvicorn>=0.37.0",
        "typer>=0.12.3",
        "pydantic>=2.11.0",
    ],
    entry_points={
        "console_scripts": [
            "kalibr=kalibr.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    include_package_data=True,
)
