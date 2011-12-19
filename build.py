'''
entry point for deployment packaging, and automated testing
author info@jbbs-inc.com
'''

#python specific
import tempfile
import subprocess
import shlex
import os
import sys
import pdb
import time
#python 2.7 specific
import argparse

#python 3rd party

#cpf specific


def log(message = "", debug = 1):
    if debug == 1:
        sys.stderr.flush()
        sys.stdout.flush()
        print message
        sys.stderr.flush()
        sys.stdout.flush()
    else:
        pass

def checkvirtualenv():
    """
    checks to make sure that virtualenv is installed
    TODO if it is not found then install 1.6.4
    """
    try:
        import virtualenv
    except:
        log("Error: virtualenv python module not found, please download from http://pypi.python.org/pypi/virtualenv and install with python setup.py install")
        sys.exit(1)
        
def createvirtualenv():
    """
    This creates a virtualenv in a temporary location
    """
    tmpdir = tempfile.mkdtemp()
    vcmd = ""
    if sys.platform.startswith('win32'):
        vcmd = "python -m virtualenv %s" %(tmpdir)
    else:
        vcmd = "virtualenv %s" %(tmpdir)
    subprocess.call( vcmd.split(" ") )
    return tmpdir

def install_deps(tmpdir = ""):
    """
    installs nose coverage selenium pymongo
    requires an internet connection
    TODO: if already installed skip
    TODO: return a list of dependancies that failed to install
    """
    ret = ""
    """
    try:
        import nose
        import coverage
        import selenium
        import mongo
    except:    
    """
    #TODO migrate to pip instead of easy_install
    # Set the location of easy_install based on platform
    targetDir = ""
    cmd = ""
    if sys.platform.startswith('win32'):
        targetDir = "Scripts"
        cmd = "%s pymongo nose" %( os.path.join(tmpdir, targetDir, "easy_install") )
    else:
        targetDir = "bin"
        cmd = "%s pymongo coverage nose" %( os.path.join(tmpdir, targetDir, "easy_install") )
    log( "Installing coverage nose and selenium into a virtualenv.")
    log( cmd )
    subprocess.call( cmd.split( " " ) )

    return ret

def install_modules(tmpdir = "", dep_return = "", testfile = "testutils.py", nose = False, nose_coverage_html = "/tmp/pythonUnitCoverage"):
    """
    installs cpf python modules into virtualenv
    runs unit tests
    """
    ret = 0
    current_dir = os.path.abspath( os.path.curdir )
    
    #case for running from with in jenkins
    if 'jenkins' in current_dir:
        log("Error: Command line options not yet implemented!")
        return 1
    

    targetDir = ""
    if sys.platform.startswith('win32'):
        targetDir = "Scripts"
    else:
        targetDir = "bin"
    
    cmd = os.path.join(tmpdir, targetDir, "python")
    
    #catches the case for using the native python and not a virualenv 
    #if tmpdir == "":
    #    cmd = "python"
    
    install_cmd = "%s setup.py install" %(cmd)
   
    #the location of the python module
    module = os.path.abspath( os.path.join(current_dir,"utils") )
    
    testfilepy = os.path.abspath( os.path.join(module, "tests", testfile) )
    if not os.path.exists(testfilepy):
        log("Error: test file (%s) does not exist" %(testfilepy))
        return 1


    os.chdir(module)
    install_cmd = "%s setup.py install" %(cmd)
    try:
        ret = subprocess.call( install_cmd.split( " " ) )
    except:
        log("\n\nError:  Was not able to install python module\n\n")
    os.chdir(current_dir)

    if sys.platform.startswith('win32'):
        unit_cmd = "%s -v --exe %s" %(os.path.join(tmpdir, targetDir, "nosetests"), module )
    else:
        if nose:
            log("\n\nRunning unit tests\n\n")
            #clean up old code coverage
            cmd = "rm -rvf %s" %(nose_coverage_html)
            subprocess.call(cmd.split(" "))
            #create directory
            cmd = "mkdir -p %s" %(nose_coverage_html)
            subprocess.call(cmd.split(" "))

            #this running through all tests in the tests directory
            unit_cmd = "%s -v --cover-html --cover-html-dir=%s --cover-package=utils --cover-tests --with-coverage --cover-erase --exe %s" \
                            %( os.path.join( tmpdir, targetDir, "nosetests" ), nose_coverage_html, testfilepy )
        else:   
            log("\n\nExecuting (%s) via python virtualenv\n\n" %(testfilepy) )
            #this runs only a single testfile that we specified via python so no unit testsing stuff stats
            unit_cmd = "%s %s" %(os.path.join(tmpdir, targetDir, "python"), testfilepy )
        
    #TODO fix as this is kind of hacky
    os.chdir(module)
    try:
        log( unit_cmd + "\n\n" ) 
        ret = subprocess.call( unit_cmd.split( " " ) )
        #if python unit testing show coverage report
        #if nose:
        #    cmd = "open %s/index.html" %(nose_coverage_html)
        #    subprocess.Popen( cmd.split(" "), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            
    except:
        log("Error:Unit tests for %s had problems\n\n" %(module) )
    #TODO fix as this is kind of hacky
    os.chdir(current_dir)
    
    #clean up
    del module
    del install_cmd
    return ret

    
def main():
    """
    main method that calls into all other methods
    """
    ret = 0
    runpythonunit = False

    phpunit_args = ""
    bHelp = 'unit test python utils module'
    #builds up command line arguments
    parser = argparse.ArgumentParser(description='Command line options')
    parser.add_argument('--unit', '-b', dest='pythonUnit', action = 'store_true', help=bHelp)
    
    #parse command line options
    args = parser.parse_args()
    if args.pythonUnit:
        runpythonunit = True
    else:
        parser.print_help()
    
    if runpythonunit == True:
        log("\n\n%s\n\n" %( bHelp ) )
        checkvirtualenv()
        #creates python virtualenv and returns the path to it
        tmpdir = createvirtualenv()
        #install dependancies and return deps that could not be installed
        dep_return = install_deps(tmpdir = tmpdir)
        #installs the python modules and runs the unit tests
        ret = ret + install_modules(tmpdir = tmpdir, dep_return = dep_return, testfile = "testjbutils.py", nose = True)
        #clear out the temporary virtualenv
        log("\n\ncleaning up by removing dir (%s)\n\n" %(tmpdir) )
        subprocess.call(shlex.split("rm -rf %s" %(tmpdir)))
        #make sure the return status is reported correctly back to buildbot or command line 
    
    if not ret == 0:
        log("Error: Process returned none zero exit status, ie some thing went wrong.  If you are confused then send email to info@jbbs-inc.com")
        sys.exit(ret)

if __name__ == '__main__':
    main()

