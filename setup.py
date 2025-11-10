from setuptools import find_packages, setup
from typing import List

# constant for the editable install line
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    Also removes the '-e .' line (editable mode instruction).
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # remove newline characters from each line
        requirements = [req.replace("\n", "") for req in requirements]

        # if '-e .' is present, remove it
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
