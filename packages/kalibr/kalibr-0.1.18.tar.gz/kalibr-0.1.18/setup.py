from setuptools import setup, find_packages

setup(
    name="kalibr",
    version="0.1.18",
    description="Kalibr SDK – expose once, run everywhere (GPT, Claude, MCP)",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic"
    ],
    entry_points={
        "console_scripts": [
            "kalibr=kalibr.__main__:main",
        ],
    },
    python_requires=">=3.8",
)
