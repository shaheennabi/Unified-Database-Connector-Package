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
            requirements = [req.strip() for req in requirements]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")
    return requirements

__version__ = "0.0.3"
REPO_NAME = "Unified-Database-Connector-Package"
PKG_NAME = "database_automator"  # Change to lowercase
AUTHOR_USER_NAME = "shaheennabi"
AUTHOR_EMAIL = "ishaheennabi333@gmail.com"

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for connecting with databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["pymongo","pymongo[srv]","dnspython", "pandas", "numpy", "ensure", "pytest"],
    include_package_data=True,
    zip_safe=False, 
)
