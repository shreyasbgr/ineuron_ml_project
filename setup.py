from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Shreyas Banagar"
DESCRIPTION="This is the first ML end-to-end ML project of iNeuron"
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function reads the requirements.txt file and returns a list of strings having all the package requirements for the project.
    return type: List[str]
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")




setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())