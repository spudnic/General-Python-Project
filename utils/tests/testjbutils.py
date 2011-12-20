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

class testClassAttributes(unittest.TestCase):
    def setUp(self):
        pass

    def test_import(self):
        try:
            import jbutils
        except:
            print "Error: not able to import jbutils make sure that the module in installed correctly"
    def test_main(self):
        import jbutils
        jbutils.main()
    
    def tearDown(self):
        """
        cleanup 
        """
        pass
    
if __name__ == '__main__':
    unittest.main()
