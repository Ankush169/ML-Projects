from setuptools import find_packages, setup
from typing import List

Hypen_e_dot = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return set of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # for reading the requirements.py file
        requirements = [req.replace("\n", " ") for req in requirements if req.strip() != Hypen_e_dot]  # exclude -e . from requirements

    return requirements

setup(
    name='MLProjects',
    version='0.0.1',
    author='Ankush',
    author_email='ankushverma1692002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
