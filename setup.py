#!/usr/bin/env python

from setuptools import setup

setup(
    name='pyflann3',
    version='1.8.4',
    description='pyflann is the python bindings for FLANN - Fast Library for Approximate Nearest Neighbors.',
    author='Marius Muja & Gefu Tang',
    author_email='mariusm@cs.ubc.ca, tanggefu@gmail.com',
    license='BSD',
    keywords="flann",
    url='https://github.com/primetang/pyflann',
    packages=['pyflann', 'pyflann.io', 'pyflann.bindings',
              'pyflann.util', 'pyflann.lib'],
    package_dir={'pyflann.lib': 'pyflann/lib'},
    package_data={'pyflann.lib': ['darwin/*.dylib', 'linux/*.so']},
)
