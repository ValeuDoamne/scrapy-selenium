"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages

def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements

    """
    with open(source) as reqs:
        install_reqs = reqs.read().strip().split('\n')
        return install_reqs

setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)
