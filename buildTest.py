#!/usr/bin/env python

#--------------------------
#@author info@jbbs-inc.com  
#unit test build.py
#--------------------------

#python internal
import unittest
import subprocess

#package we are testing
import build

class testClassAttributes(unittest.TestCase):
    def setUp(self):
        """
        Nothing to setup
        """
        self.tmpdir = build.createvirtualenv()

    def tearDown(self):
        """
        Nothing to cleanup 
        """
        cmd = "rm -rf %s" %(self.tmpdir) 
        subprocess.call(cmd.split(' ') )
        del self.tmpdir
    """
    def test_main(self):
        '''
        Test main with no arguments
        '''
        build.main()
    """
    
    def test_install_modules(self):
        """
        Trying to install internal python modules
        """
        build.install_modules(tmpdir = self.tmpdir, nose = True, test = True)
    
    """
    def test_install_deps(self):
        '''
        Trying to install dependancies
        '''
        build.install_deps(tmpdir = self.tmpdir, test = True)
    """

if __name__ == '__main__':
    unittest.main()

