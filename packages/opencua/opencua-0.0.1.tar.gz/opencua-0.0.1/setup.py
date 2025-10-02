from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="opencua",
    version="0.0.1",
    author="",
    author_email="",
    description="OpenCUA package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/opencua",
    packages=find_packages(where="src/python"),
    package_dir={"": "src/python"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
