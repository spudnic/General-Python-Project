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

def main():
    cmd_noreturn("ls -lart")  


