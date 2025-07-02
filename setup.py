# Install packages
from setuptools import setup,find_packages
from typing import List


hyphen_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements]
        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    description='This is production label end to end machine learning project',
    long_description=open('README.md').read(),
    author='Prince Gupta',
    author_email='princegupta878721@gmail.com',
    long_description_content_type='Markdown',
    url='https://github.com/PrinceGupta8/MLPROJECT.git',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    classifiers='python Language :3'
)


