FROM ubuntu:latest

# Installing as root: docker images are usually set up as root.
# Since some autotools scripts might complain about this being unsafe, we set
# FORCE_UNSAFE_CONFIGURE=1 to avoid configure errors.
ENV FORCE_UNSAFE_CONFIGURE=1
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y build-essential wget unzip git python3-numpy python3-numpydoc python3-scipy python3-matplotlib python3-h5py python3-pytest python3-coverage pylint sphinx
RUN apt-get autoremove -y

RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.7.0.2747-linux.zip && \
    unzip sonar-scanner-cli-4.7.0.2747-linux.zip && \
    ln -s /sonar-scanner-4.7.0.2747-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner && \
    rm /sonar-scanner-cli-4.7.0.2747-linux.zip
