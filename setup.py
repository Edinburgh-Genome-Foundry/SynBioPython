# pylint: disable=C0103,C0114, W0122
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("synbiopython/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="synbiopython",
    version=version["__version__"],
    author="Global Biofoundries Alliance",
    author_email="author@example.com",
    description="Python tools for Synthetic Biology.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://synbiopython.org",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=0.22",
        "numpy>=1.19",
        "fuzzywuzzy",
        "dnaplotlib",
        "tesedml<0.4.5.3",
        "tellurium",
        "tesbml",
        "biopython",
        "reportlab",
        "Pillow<6.0.0",
    ],
)
