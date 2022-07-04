
VERSION = $(shell cat VERSION.txt )
CWD = $(shell pwd)

build:	## builds the docker file
	docker build -t dev-python:$(VERSION) .

bash:	## run the container that has python installed
	echo $(CWD)
	docker run -it --volume $(CWD):/opt/git dev-python:$(VERSION)  /bin/bash

help:	## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
