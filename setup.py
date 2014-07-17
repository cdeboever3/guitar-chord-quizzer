import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'guitar_chord_quizzer',
    version = '0.0.1',
    author = 'Christopher DeBoever',
    author_email = 'cdeboever3@gmail.com',
    description = ('Quizzes you on guitar chords!'),
    packages=find_packages(),
)
#     license = 'BSD',
#     keywords = 'example documentation tutorial',
#     url = 'http://packages.python.org/an_example_pypi_project',
#     packages=['an_example_pypi_project', 'tests'],
#     long_description=read('README'),
#     classifiers=[
#         'Development Status :: 3 - Alpha',
#         'Topic :: Utilities',
#         'License :: OSI Approved :: BSD License',
#    ],
