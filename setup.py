import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'guitar-quizzer',
    version = '0.0.1',
    author = 'Christopher DeBoever',
    author_email = 'cdeboever3@gmail.com',
    description = ('Quizzes you on guitar stuff!'),
    packages=find_packages(),
    license = 'MIT',
    keywords = 'guitar music', 
    url = 'https://github.com/cdeboever3/guitar-quizzer',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
   ]
)
