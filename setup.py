__author__ = 'James Polera'
__since__  = '2012.05.29'
__email__  = 'james@uncryptic.com'

import os
import sys

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

settings = dict()

if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist upload')
  sys.exit()

settings.update(
  name='nameparts',
  version='0.5.2',
  description='Takes a full human name and splits it into individual parts',
  long_description=read('README.md'),
  author='James Polera',
  author_email='james@uncryptic.com',
  url='https://github.com/polera/nameparts',
  keywords='name text processing',
  py_modules=['nameparts',],
  license='BSD',
  classifiers=(
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
  )
)

setup(**settings)