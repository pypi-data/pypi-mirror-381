from setuptools import setup, find_packages

setup(
    name="kalibr",
    version="0.1.16",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "kalibr=kalibr.__main__:main",
        ],
    },
)
