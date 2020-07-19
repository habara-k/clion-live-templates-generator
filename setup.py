from setuptools import find_packages, setup
from codecs import open
from os import path

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='clion-live-templates-generator',

    version='1.0.3',

    license='MIT',

    author='Keigo Habara',
    author_email='k.habara.aa@gmail.com',

    url='https://github.com/habara-k/clion-live-templates-generator',

    description="Generate CLion's Live templates from a library of competitive programming",
    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'lt-generate = clion_live_templates_generator.main:main',
        ],
    },
)
