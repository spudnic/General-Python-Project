#!/usr/bin/env python

#--------------------------
#@author info@jbbs-inc.com  
#unit test build.py
#--------------------------

import build

class testClassAttributes(unittest.TestCase):
    def setUp(self):
        """
        Nothing to setup
        """
        pass

    def tearDown(self):
        """
        Nothing to cleanup 
        """
        pass

    def test_main():
        """
        Test main with no arguments
        """
        build.main()


if __name__ == '__main__':
    unittest.main()

