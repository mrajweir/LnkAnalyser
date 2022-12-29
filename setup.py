import setuptools
import json

# Collect the version information from the version file. This project is autobumped.
with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("version", "r") as vh:
    version_file = json.load(vh)
    version = "{}.{}.{}".format(
        version_file["major"],
        version_file["minor"],
        version_file["micro"]
    )

setuptools.setup(
    name="LnkAnalyser",
    version=version,
    author="Andrew Weir",
    author_email="andrew@ajweir.co.uk",
    description="A Python package for analysing Windows shortcut files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ajweir.co.uk/projects/lnk-analyser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)