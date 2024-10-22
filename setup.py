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



# Read long description from README.md
try:
    with open('README.md', encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A Python package for connecting with databases."

setup(
    name="db_crud_automated",
    version="0.0.10",
    author="shaheennabi",
    author_email="ishaheennabi333@gmail.com",
    description="A Python package for connecting with databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaheennabi/Unified-Database-Connector-Package",
    packages=find_packages(where="src"),  
    package_dir={"": "src"},
    install_requires=["pymongo","pandas", "numpy", "dnspython", "pytest"],
    include_package_data=True,
    zip_safe=False,
)
