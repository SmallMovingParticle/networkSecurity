from setuptools import find_packages , setup ##find_packages considers all the folders with __init__ and the folder that has init act as a package
from typing import List





def get_requirements()->List[str]:
    ## this function return the list of requirements

    try:
        with open('requirements.txt', 'r') as file:
            ## read lines
            lines=file.readlines()
            requirement_lst:List[str]=[]
            ##process line
            for line in lines:
                requirement=line.strip()

                ##ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirement.txt file not foud")

    return requirement_lst

print(get_requirements())




setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Devyansh chadhary",
    author_email="chaudharydivyansh04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)