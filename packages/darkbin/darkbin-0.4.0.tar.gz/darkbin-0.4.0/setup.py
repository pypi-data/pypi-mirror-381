from setuptools import setup

setup(
    name="darkbin",          # package name (same as before)
    version="0.4.0",         # new version!
    py_modules=["darkbin"],  # since it’s a single file
    install_requires=[],      # add dependencies if any
    entry_points={
        "console_scripts": [
            "darkbin=darkbin:main",  # your main function
        ],
    },
    author="Your Name",
    author_email="you@example.com",
    description="Darkbin updated version",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/darkbin",  # optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
