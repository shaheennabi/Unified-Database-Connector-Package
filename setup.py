from setuptools import setup, find_packages
from typing import List
import os

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements file and returns a list of dependencies."""
    requirements = []
    if os.path.exists(file_path):
        with open(file_path, encoding="utf-8") as f:
            requirements = f.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")
    return requirements

# Modify this to point to the correct requirements file
requirements = get_requirements('requirements.txt')  # or 'requirements_dev.txt'

setup(
    name="Database Automator",
    version="0.0.3",
    author="shaheennabi",
    author_email="ishaheennabi333@gmail.com",
    description="A Python package for connecting with databases.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shaheennabi/Unified-Database-Connector-Package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)
