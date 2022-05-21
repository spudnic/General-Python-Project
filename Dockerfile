FROM python:3.8.13

# Install kubectl from Docker Hub.
COPY --from=lachlanevenson/k8s-kubectl:v1.10.3 /usr/local/bin/kubectl /usr/local/bin/kubectl

WORKDIR /opt/work

COPY build.py /opt/work
COPY utils /opt/work/utils
RUN pip install --upgrade pip
RUN python build.py -b
