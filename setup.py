'''
this setup file is essential part for packaging and  distributing python packages .
it is used  by the Python packaging ecosystem to identify the package and its dependencies.
to define the configuration og the project  , such as its meta data , dependencies , and more
''' 

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Get the list of requirements from a requirements file.
    """
    requirement_list = []
    try:
            with open('requirements.txt', "r") as file:
                lines = file.readlines()
                for line in lines:
                    requirement = line.strip()
                    if requirement and requirement != '-e .':
                        requirement_list.append(requirement)

    except FileNotFoundError:
        print(f"File not found:")

    return requirement_list

print(get_requirements())




setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Dixit",
    author_email="dixit57155@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
