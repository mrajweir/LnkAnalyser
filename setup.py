import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LnkAnalyser",
    version="0.1",
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