from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ValorantApiPy',
    version='1.0.0',
    description='API wrapper in python of valorant-api(Not an official valorant api)',
    url='https://github.com/sanskark/python-wrapper',
    author='Sanskar Khunt',
    author_email='sanskarkhunt42@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)