# General Python module
This project is an example python module developed with test driven development. We strive to keep 80% code coverage as we add more to the module.
<BR><BR> Build Status main branch [![Build Status main](https://github.com/spudnic/General-Python-Project/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/spudnic/General-Python-Project/actions/workflows/main.yml)

## If you have python installed

```bash
$ python3 build.py 
usage: build.py [-h] [--unit] [--unit-fast] [--docker-build]

Command Line Options

optional arguments:
  -h, --help          show this help message and exit
  --unit, -b          Full tests, run locally
  --unit-fast, -f     Full tests, run locally, no network connection
  --docker-build, -d  build with in a docker container

$ python build.py -b
created virtual environment CPython3.8.13.final.0-64 in 108ms
...
----------------------------------------------------------------------
XML: /opt/work/utils/nosetests.xml
Name                  Stmts   Miss  Cover
-----------------------------------------
jbutils/__init__.py      50      0   100%
-----------------------------------------
TOTAL                    50      0   100%
----------------------------------------------------------------------
Ran 8 tests in 0.033s
OK
cleaning up by removing dir (/tmp/tmpof_cqvkv)

$ 
```

## If you only have docker installed and no python

```bash
% make help
build:   builds the docker file
bash:    run the container that has python installed
help:    Show this help.

% make bash
docker build -t dev-python:0.0.1 .
[+] Building 2.2s (13/13) FINISHED  
...                                                                                                                                                                            
echo /Users/brody/workspace/github.com/spudnic/General-Python-Project
/Users/brody/workspace/github.com/spudnic/General-Python-Project
docker run -it --volume /Users/brody/workspace/github.com/spudnic/General-Python-Project:/opt/git dev-python:0.0.1  /bin/bash

root@cb4f72fe0a36:/opt/work# python build.py 
usage: build.py [-h] [--unit] [--unit-fast] [--docker-build]

Command Line Options

optional arguments:
  -h, --help          show this help message and exit
  --unit, -b          Full tests, run locally
  --unit-fast, -f     Full tests, run locally, no network connection
  --docker-build, -d  build with in a docker container
root@cb4f72fe0a36:/opt/work# python build.py -b
created virtual environment CPython3.8.13.final.0-64 in 108ms
...
----------------------------------------------------------------------
XML: /opt/work/utils/nosetests.xml
Name                  Stmts   Miss  Cover
-----------------------------------------
jbutils/__init__.py      50      0   100%
-----------------------------------------
TOTAL                    50      0   100%
----------------------------------------------------------------------
Ran 8 tests in 0.033s
OK
cleaning up by removing dir (/tmp/tmpof_cqvkv)
root@7efb64cbb1c0:/opt/work# 
```

