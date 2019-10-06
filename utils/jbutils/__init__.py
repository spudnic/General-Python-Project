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

 
def cmd_noreturn(cmd = "", test = False):
    if test:
        print('In Test Mode: command(', cmd, ')')
    else:
        p = subprocess.Popen(cmd.split(" "), stdout = subprocess.PIPE, stderr = subprocess.PIPE)

def checkk8():
    cmd_noreturn("/usr/local/bin/kubectl get svc")

def main():
    test = False
    from argparse import ArgumentParser
    parser = ArgumentParser(description = 'Command Line Options')
    parser.add_argument('--test-env', '-a', dest='test', action = 'store_true', help='Dump the environment')
    parser.add_argument('--kubectl-verify', '-b', dest='b', action='store_true', help='verify that kubectl is configured to talk to a k8 cluster and display connection information')
    parser.add_argument('--build-container', '-c', dest='c', action='store_true',
                        help='build the docker container, assumes the Dockerfile is at root')
    options = parser.parse_args()
    
    if len(sys.argv) < 2:
        parser.print_help()
        
    if options.test:
        test = True
        cmd_noreturn("ls -lart")  
    
    if options.b:
        checkk8()
  
    


