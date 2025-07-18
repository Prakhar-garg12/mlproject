##  with the help of setup.py i am able to build macine learning project as a package, we can use this package anywhere
#  we can install this package using pip install command

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Prakhar',
author_email='prakhargarg0611@gmail.com',
packages=find_packages(), ## find_packages() ka kaam hai:
##👉 Automatically tumhare project ke andar sabhi Python packages (folders) ko dhoondhna jo install hone chahiye.
# install_requires=['pandas','numpy','seaborn']


install_requires=get_requirements('requirements.txt')

)