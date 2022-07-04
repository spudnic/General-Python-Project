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
$ 
```

## If you only have docker installed and no python

```bash
% make help
build:   builds the docker file
bash:    run the container that has python installed
help:    Show this help.
% 
```

