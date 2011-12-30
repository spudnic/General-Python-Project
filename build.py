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

#python 3rd party

#internal


def log(message = "", debug = 1):
    if debug == 1:
        sys.stderr.flush()
        sys.stdout.flush()
        print(message)
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
    except ImportError:
        log("Warning: virtualenv python module not found, installing with pip")
        cmd = "pip install virtualenv"
        subprocess.call( cmd.split( " " ) )
        
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

def install_deps(tmpdir = "", test = False):
    """
    installs dependances
    requires an internet connection
    TODO: if already installed skip
    TODO: return a list of dependancies that failed to install
    """
    ret = 0
    """
    try:
        import nose
        import coverage
    except:    
    """
    targetDir = ""
    cmd = ""
    if sys.platform.startswith('win32'):
        targetDir = "Scripts"
        cmd = "%s install pymongo nose" %( os.path.join(tmpdir, targetDir, "pip") )
    else:
        targetDir = "bin"
        cmd = "%s install coverage nose" %( os.path.join(tmpdir, targetDir, "pip") )
    log( "Installing coverage and nose into a virtualenv.")
    log( cmd )
    if not test:
        ret = subprocess.call( cmd.split( " " ) )

    return ret
def getTargetDir():
    if sys.platform.startswith('win32'):
        targetDir = "Scripts"
    else:
        targetDir = "bin"
    return targetDir

def install_modules(test = False, tmpdir = "", dep_return = "", testfile = "testjbutils.py", nose = False, nose_coverage_html = "/tmp/pythonUnitCoverage"):
    """
    installs cpf python modules into virtualenv
    runs unit tests
    """
    ret = 0
    current_dir = os.path.abspath( os.path.curdir )
    module = os.path.abspath( os.path.join(current_dir, "utils") )
    targetDir = getTargetDir()
    
    cmd = os.path.join(tmpdir, targetDir, "python")
    bundle_cmd = os.path.join(tmpdir, targetDir, "pip")
    
    #make the bundle
    bundle_cmd = bundle_cmd + " bundle jbutils.pybundle ."
    if test:
        log("\n\n %s \n\n" %(bundle_cmd) )
    else:
        os.chdir(module)
        try:
            ret = subprocess.call( bundle_cmd.split( " " ) )
        except:
            log("\n\nError:  Was not able to pip bundle python module\n\n")
        os.chdir(current_dir)
    
    #install the bundle
    install_cmd = os.path.join(tmpdir, targetDir, "pip")
    install_cmd = install_cmd + " install jbutils.pybundle --upgrade"
    if test:
        log("\n\n %s \n\n" %(install_cmd) )
    else:
        os.chdir(module)
        try:
            ret = subprocess.call( install_cmd.split( " " ) )
        except:
            log("\n\nError:  Was not able to pip install python module\n\n")
        os.chdir(current_dir)

    if not ret == 0:
        return ret 
    else: 
        ret = run_test(test = test, tmpdir = tmpdir, dep_return = dep_return, testfile = testfile, nose = nose, nose_coverage_html = nose_coverage_html)
    return ret

def run_test(test = False, tmpdir = "", dep_return = "", testfile = "testjbutils.py", nose = False, nose_coverage_html = "/tmp/pythonUnitCoverage"):
    ret = 0
    #the location of the python module
    current_dir = os.path.abspath( os.path.curdir )
    module = os.path.abspath( os.path.join(current_dir, "utils") )
    targetDir = ""
    if sys.platform.startswith('win32'):
        targetDir = "Scripts"
    else:
        targetDir = "bin"
    

    #testfilepy = os.path.abspath( os.path.join(module, "tests", testfile) )
    testfilepy = os.path.abspath( os.path.join(module, "tests") )
    if not os.path.exists(testfilepy):
        log("Error: test file (%s) does not exist" %(testfilepy))
        return 1

    
    if sys.platform.startswith('win32'):
        unit_cmd = "%s -v --exe %s" %(os.path.join(tmpdir, targetDir, "nosetests"), module )
    else:
        if nose:
            log("\n\nRunning unit tests\n\n")
            #clean up old code coverage
            if os.path.exists(nose_coverage_html):
                cmd = "rm -rvf %s" %(nose_coverage_html)
                subprocess.call(cmd.split(" "))
            #create directory
            cmd = "mkdir -p %s" %(nose_coverage_html)
            if test:
                log("\n\n %s \n\nz" %(cmd) )
            else:
                subprocess.call(cmd.split(" "))

            #running through all tests in the tests directory
            unit_cmd = "%s -v --cover-package=jbutils --cover-tests --with-coverage --cover-erase --with-xunit --exe %s" \
                            %( os.path.join( tmpdir, targetDir, "nosetests" ), testfilepy )
        else:   
            log("\n\nExecuting (%s) via python virtualenv\n\n" %(testfilepy) )
            #this runs only a single testfile that we specified via python so no unit testsing stuff stats
            unit_cmd = "%s %s" %(os.path.join(tmpdir, targetDir, "python"), testfilepy )
        
    #TODO fix as this is kind of hacky
    if test:
        log("\n\n %s \n\n" %(unit_cmd) )
    else:
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
        
    return ret

def get_python():
    """
    locates the current installation of python virtual env
    """
    #TODO make this more robust
    python = os.environ["VIRTUAL_ENV"]
    return python

def remove_module(tmpdir = "", module = ""):
    ret = 0
    #the location of the python module
    current_dir = os.path.abspath( os.path.curdir )
    targetDir = getTargetDir()
    remove_cmd = os.path.join(tmpdir, targetDir, "pip")
    remove_cmd += " uninstall %s" %(module)
    log("\n\n%s\n\n" %(remove_cmd) )
    ret = subprocess.call(remove_cmd.split(' ') )
    return ret

def main():
    """
    main method that calls into all other methods
    """
    ret = 0
    runpythonunit = False
    runpythonunitfast = False
    bHelp = 'Full test'
    fHelp = 'Full tests, no network connection'
    des = "Command Line Options"
    phpunit_args = ""
    #builds up command line arguments
    try:
        from argparse import ArgumentParser
        parser = ArgumentParser(description = des)
        parser.add_argument('--unit', '-b', dest='u', action = 'store_true', help=bHelp)
        parser.add_argument('--unit-fast', '-f', dest='f', action = 'store_true', help=fHelp)
        args = parser.parse_args()
        
    except ImportError: #Must be python 2.6 or lower
        from optparse import OptionParser
        parser = OptionParser(description = des)
        parser.add_option('--unit', '-b', dest='u', action = 'store_true', help=bHelp)
        parser.add_option('--unit-fast', '-f', dest='f', action = 'store_true', help=fHelp)
        args, blank  = parser.parse_args()
       
    #parse command line options
    if args.u:
        runpythonunit = True
    if args.f:
        runpythonunitfast = True
    
    if len(sys.argv) < 2:
        parser.print_help()
    
    if runpythonunitfast == True:
        #get the location of current virtualenv
        local_python = get_python()
        #install dependancies and return deps that could not be installed
        ret = install_modules(tmpdir = local_python, nose = True)
        remove_module(tmpdir = local_python, module = 'jbutils')
    
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


