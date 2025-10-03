from setuptools import setup, find_packages

setup(
    name="kalibr",
    version="0.1.13",
    packages=find_packages(),
    install_requires=["fastapi", "uvicorn"],
    entry_points={
        "console_scripts": [
            "kalibr-demo=__main__:main",
        ],
    },
)
