from setuptools import setup, find_packages

setup(
    name="darkbin",
    version="0.2.0",
    description="DarkBin - BIN lookup & CC extractor",
    author="Darkboy",
    author_email="your_email@example.com",
    url="https://github.com/d0x-dev/darkbin",
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "darkbin=darkbin.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
