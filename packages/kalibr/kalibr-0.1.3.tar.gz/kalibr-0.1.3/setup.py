from setuptools import setup, find_packages

setup(
    name="kalibr",  # package name on PyPI
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "kalibr-demo=kalibr.__main__:main"
        ]
    },
    author="Kalibr",
    description="SDK for making SaaS agent-ready with 7 lines of code",
    url="https://kalibr.systems",
    python_requires=">=3.8",
)
