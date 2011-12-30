#!/usr/bin/env python

#--------------------------
#@author info@jbbs-inc.com  
#unit tests
#--------------------------

#python specific
import unittest
import os
import tempfile
import subprocess
import shlex
import pdb
import string
import sys

class testClassAttributes(unittest.TestCase):
    def setUp(self):
        pass

    def test_import(self):
        '''
        import the module
        '''
        try:
            import jbutils
        except:
            print "Error: not able to import jbutils make sure that the module in installed correctly"

    def test_main(self):
        '''
        execute main
        '''
        import jbutils
        old_args = sys.argv
        sys.argv = ['--test-env']
        jbutils.main()
        sys.argv = old_args
    
    def test_commandline(self):
        '''
        run via the command line
        '''
        pass
        """ this causes errors when run from build.py
        if sys.platform.startswith('win32'):
            subprocess.call('jbutilsrun.bat')
        else:
            subprocess.call('jbutilsrun')
        """
    def tearDown(self):
        """
        cleanup 
        """
        pass
    
if __name__ == '__main__':
    unittest.main()
