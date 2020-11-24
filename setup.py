# Script Setup Wibas 
# Package Library focused Web,AI,Android and IOS
# Author : Ananda Rauf Maududi
# Licence :  MIT Licence and UUD Copyright.


import sys
from setuptools import setup
from os.path import dirname, join
import codecs
import os
import re
import io

here = os.path.abspath(os.path.dirname(__file__))

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
=================================
Sorry unsupported Python version
=================================
Wibas requires Python {}.{}, please
install Python version {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

def finding_version(*file_paths):
    with codecs.open(os.path.join(here, *file_paths), 'r', 'utf-8') as f:
        version_file = f.read()

        version_match = re.search(r"^__versi__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
      name='Wibas',
      version=finding_version('Wibas','wibas.py'),
      description='Wibas',
      long_description='Wibas is library packages for focused Web,AI,Android and IOS',
      devdate='24 November 2020'
      author='Ananda Rauf Maududi',
      author_instagram='https://www.instagram.com/anandaraufm'
      url_code='https://www.github.com/AnandaRauf/Wibas'
      licence='MIT and UUD Copyright'
      packages=['Wibas'],
      install_requires=['pexpect', 'virtualenv', 'sh'],
      classifiers=[
        'Development Status :: 5 - Production/Stable', 
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
      )
