from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = '-e .'


def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    return requirements
setup(
    name='restaurant_recommnedation',
    version='0.1.0',
    author='Aditya',
    author_email='ag82620790@gmail.com',
    packages=find_packages(),
    install_requires=[]
)