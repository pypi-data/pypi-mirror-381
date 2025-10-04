from setuptools import setup, find_packages

setup(
    name="kalibr",
    version="0.1.21",
    description="Kalibr Demo SDK",
    author="Devon Kelley",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "typer",   # CLI framework
    ],
    entry_points={
        "console_scripts": [
            "kalibr=kalibr.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
