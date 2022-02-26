import os
from setuptools import find_packages, setup
from importlib.machinery import SourceFileLoader
from typing import List


module_name = 'lgint'
module = SourceFileLoader(
    module_name,
    os.path.join(module_name, '__init__.py'),
).load_module()


def parse_requirements(filename: str) -> List[str]:
    requirements = list()
    with open(filename) as file:
        for line in file:
            requirements.append(line.rstrip())
    return requirements


setup(
    name=module_name,
    version=module.__version__,
    author=module.__author__,
    author_email=module.__email__,
    url='https://github.com/churilov-ns/lgint.git',
    license=module.__license__,
    description=module.__doc__,
    long_description=open('README.md').read(),
    classifiers=[
        'Intended Audience :: Science/Research',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Astronomy',
    ],
    platforms='all',
    python_requires='>=3.8',
    packages=find_packages(exclude=['tests']),
    install_requires=parse_requirements('requirements.txt'),
    extras_require={'dev': parse_requirements('requirements.dev.txt')},
    include_package_data=True,
)
