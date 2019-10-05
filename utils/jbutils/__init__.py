'''
jbutils python module
author info@jbbs-inc.com
'''

#python specific
import pdb
import os
import sys
import subprocess
import time

#3rd party python specific

 
def cmd_noreturn(cmd = ""):
    p = subprocess.Popen(cmd.split(" "), stdout = subprocess.PIPE, stderr = subprocess.PIPE)

def checkk8():
    cmd_noreturn("/usr/local/bin/kubectl get svc")

def main():
    test = False
    aHelp = "Dump the environment"
    des = 'Command Line Options'
    #parse command line options

    #this will require python 2.7 and above
    from argparse import ArgumentParser
    parser = ArgumentParser(description = des)
    parser.add_argument('--test-env', '-a', dest='test', action = 'store_true', help=aHelp)

    options = parser.parse_args()
    
    if options.test:
        test = True
    else:
        parser.print_help()
        
    if test:
        cmd_noreturn("ls -lart")  
    
    cmd_noreturn("ls -lart")  
  
    


