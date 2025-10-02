from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="fulcrum-ai", 
    version="0.0.1",
    packages=find_packages(include=["fulcrum_ai", "fulcrum_ai.*"]),
    description="Public pythonsdk for Fulcrum AI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Darren Jackson",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        r.strip() for r in open(
            "_requirements/prod.txt", 
            encoding="utf-8"
        ).readlines()
    ],
)
