from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Eduard",
    author_email="edup4801@gmail.com",
    description="image processing package in Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eduardd26315/package-template-dio.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    )