#!/usr/bin/env python

#---------------------
#@author info@jbbs-inc.com
#---------------------

"""
Standard setup script.
"""

import sys
import os
import pdb
from distutils.core import setup
from distutils.core import Command
#from distutils.command.install_data import install_data
#from distutils.command.sdist import sdist

name = "jbutils"
scripts = [os.path.join( "bin","%srun"     %(name) ), \
           os.path.join( "bin","%srun.bat" %(name) )]

long_description="""
This modules try's to set a standard way to build contianers and interact with kubectl. By default it assumes you are running minikube but it can also be used to deploy to a k8 cluster. 
"""

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        cmd = 'nosetests -v --cover-html --cover-package=jbutils --cover-tests --with-coverage --cover-erase --with-xunit --exe tests/'
        errno = subprocess.call(cmd.split(' '))
        raise SystemExit(errno)

setup_args = {
    'name': name,
    'version': "1.0.0",
    'description': "kubectl and container launch in a standard way",
    'long_description': long_description,
    'author': "Brody",
    'author_email': "info@jbbs-inc.com",
    'url': "http://jbbs-inc.com",
    'license': "GNU GPL",
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

setup(  cmdclass = {'test': PyTest},**setup_args)

