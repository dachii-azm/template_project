from setuptools import setup, find_packages

setup(
    name='prj',
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'prj': ['*.txt', '*.md', '*.json', '*.yaml', '*.yml'],
    },
    install_requires=[
        'matplotlib>=3.4.0',
    ],
)
