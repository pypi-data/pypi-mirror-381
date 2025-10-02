from setuptools import setup, find_packages

setup(
    name='PyBahn',
    version='0.1.12',
    packages=find_packages(),
    install_requires=[
        "requests",
        "reportlab"
    ]
)
