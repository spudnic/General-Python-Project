#!/usr/bin/env python

#---------------------
#@author info@jbbs-inc.com
#---------------------

"""
Standard setup script.
"""

import sys
import os

from distutils.core import setup
#from distutils.command.install_data import install_data
#from distutils.command.sdist import sdist

name = "jbutils"
scripts = [os.path.join( "bin","%srun"     %(name) ), \
           os.path.join( "bin","%srun.bat" %(name) )]

long_description="""
This modules is a sample of test driven development.
"""

setup_args = {
    'name': name,
    'version': "1.0.0",
    'description': "utils Python Module",
    'long_description': long_description,
    'author': "Brody",
    'author_email': "info@jbbs-inc.com",
    'url': "http://jbbs-inc.com",
    'license': "GNU GPL",
    # does this classifiers= mean that this can't be installed on 2.2/2.3?
    'classifiers': [
        'Development Status :: 4 - Beta/Stable',
        'Environment :: Local Application OSX Linux Windows',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Software Development :: Utilities library',
        ],

    'packages': [name], 
    'scripts': scripts,
}

# set zip_safe to false to force Windows installs to always unpack eggs
# into directories, which seems to work better --
if sys.platform == "win32":
    setup_args['zip_safe'] = False


setup(**setup_args)

