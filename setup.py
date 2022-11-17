
from setuptools import setup

setup(
        name='jackattack', # this is what you 'pip install'
        version='0.0.1',
        description='An attack class for Jack',
        py_modules=["jackattack"], # this is what you will import
        package_dir=['':'src'],
)
