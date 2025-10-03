# setup.py
from setuptools import setup, find_packages

setup(
    name="kalibr",
    version="0.1.15",
    description="Kalibr SDK – expose once, run everywhere (GPT, Claude, MCP)",
    packages=find_packages(),
    install_requires=["fastapi", "uvicorn", "pydantic"],
    entry_points={
        "console_scripts": [
            "kalibr=kalibr.__main__:main",
        ],
    },
    python_requires=">=3.8",
)
