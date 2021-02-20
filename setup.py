import setuptools
from importlib import import_module


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='persian_tools',
    packages=setuptools.find_packages(),
    version=import_module('persian_tools').__version__,
    license='MIT',
    description='An anthology of a variety of tools for the Persian language in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ali Madihi (mrunderline)',
    author_email='alimadihib@gmail.com',
    url='https://github.com/persian-tools/py-persian-tools',
    keywords=['digits', 'commas', 'iranian bank', 'card number', 'national id', 'national code', 'ordinal suffix'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities'
    ],
)
