import os
import json
from setuptools import find_packages, setup

setup(
    name="learnkanada",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="Learn Kanada one word a day",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'gui_scripts': ['kanada = learnkanada:main']
    }
)
