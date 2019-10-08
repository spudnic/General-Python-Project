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
        # create empty Dockerfile
        os.system('touch Dockerfile')

    def test_import(self):
        '''
        import the module
        '''
        try:
            import jbutils
        except:
            print("Error: not able to import jbutils make sure that the module in installed correctly")

    def test_main(self):
        '''
        execute main
        '''
        import jbutils
        old_args = sys.argv
        sys.argv = ['jbutilsrun','--test-env', '-b', '-c', '-d']
        jbutils.main()
        sys.argv = old_args

    def test_cmd_return(self):
        import jbutils
        jbutils.cmd_return(test=True)
        jbutils.cmd_return(cmd="ls -lart")

    def test_cmd_noreturn(self):
        import jbutils
        jbutils.cmd_noreturn(test=True)
        jbutils.cmd_noreturn(cmd="ls -lart")

    def test_printhelp(self):
        '''
        print the help
        '''
        import jbutils
        old_args = sys.argv
        sys.argv = ['jbutilsrun']
        jbutils.main()
        sys.argv = old_args

    def test_checkk8(self):
        '''
        run some basic kubectl
        '''
        import jbutils
        jbutils.checkk8(test=True)

    def test_dockerbuild(self):
        '''
        try to build the container
        '''
        import jbutils
        jbutils.dockerbuild(path='Dockerfile', test=True)

        # we expect this to return error
        try:
            jbutils.dockerbuild(path='badfile')
        except:
            pass

    def test_dockerrun(self):
        '''
        try to run the container
        '''
        import jbutils
        jbutils.dockerrun(containername='app:1', test=True)


    def tearDown(self):
        """
        cleanup 
        """
        os.system('rm Dockerfile')
    
if __name__ == '__main__':
    unittest.main()
