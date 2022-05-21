'''
jbutils python module
author info@jbbs-inc.com
'''

#python specific
import os
import sys
import subprocess
import time

#3rd party python specific

def cmd_return(cmd = "", test = False):
    if test:
        print('In Test Mode: command( ', cmd, ' )')
    else:
        print('----About to run \n' + cmd)
        p = subprocess.call(cmd.split(" "))
        print('----Done')
        return p

def cmd_noreturn(cmd = "", test = False):
    if test:
        print('In Test Mode: command( ', cmd, ' )')
    else:
        print('----About to run \n' + cmd )
        subprocess.Popen(cmd.split(" "), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        print('----Done')

def checkk8(containername = 'app:1', test = False):
    # cmd_return("/usr/local/bin/kubectl get svc", test=test)
    dockerrun(containername=containername, cmd = '/usr/local/bin/kubectl', test = test)

def dockerrun(containername = 'app:1', cmd = 'bash', test = False ):
    h = os.environ['HOME']
    cmd = 'docker run -v '+ h +'/.kube:/root/.kube -v ' + h + '/.minikube:'+ h +'/.minikube -it ' + containername + ' ' + cmd
    cmd_return(cmd=cmd, test=test)

def dockerbuild(path = 'Dockerfile', containername = "app:1", test = False):
    '''
    Check for the existence of a Dockerfile
    build it
    :return:
    '''
    if os.path.exists(path):
        cmd = 'docker build -f ' + path + ' -t ' + containername + ' .'
        cmd_return(cmd, test)
    else:
        d = os.getcwd()
        print('Error: Dockerfile not found at (', d + os.path.sep + path, ')')
        exit(1)

def main():
    test = False
    containername = 'app:1'
    from argparse import ArgumentParser
    parser = ArgumentParser(description = 'Command Line Options')
    parser.add_argument('--test-env', '-a', dest='test', action = 'store_true', help='Dump the environment')
    parser.add_argument('--kubectl-verify', '-b', dest='b', action='store_true', help='verify that kubectl is configured to talk to a k8 cluster and display connection information')
    parser.add_argument('--build-container', '-c', dest='c', action='store_true',
                        help='build the docker container, assumes the Dockerfile is at root')
    parser.add_argument('--run-container', '-d', dest='d', action='store_true',
                        help='run the docker container assumes it is already built')
    options = parser.parse_args()
    
    if len(sys.argv) < 2:
        parser.print_help()
        
    if options.test:
        test = True
    
    if options.b:
        checkk8(test=test)

    if options.c:
        dockerbuild(test=test)

    if options.d:
        dockerrun(containername=containername, test=test)
  
    


