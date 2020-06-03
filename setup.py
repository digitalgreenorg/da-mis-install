from distutils.core import setup
from setuptools import find_packages
from helpers.config import Config

setup(
    name='DigitalGreen',
    version=Config.KOBO_INSTALL_VERSION,
    packages=find_packages(exclude=['tests']),  # Include all the python modules except `tests`,
    url='https://github.com/digitalgreenorg/da-mis-install/',
    license='',
    author='DigitalGreen',
    author_email='',
    description='Installer for DA MIS System'
)
