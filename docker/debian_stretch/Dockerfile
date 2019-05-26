FROM debian:stretch-slim

LABEL desc : "This Docker file to Testing for Debian:Stretch"

#install git,
RUN apt-get update \
        && apt-get install -y --no-install-recommends git \
	#clonning vulnx
	&& git clone http://github.com/anouarbensaad/vulnx \
	#cleaning cache to build a small image size.
	    && rm -rf /var/lib/apt/lists/* \
        && apt-get clean \
        && rm -rf /tmp/* /var/tmp/* /usr/share/doc/*

#Working−Directory
WORKDIR vulnx

#install pip3
RUN apt-get update \
        && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
	    && rm -rf /var/lib/apt/lists/* \
        && apt-get clean \
        && rm -rf /tmp/* /var/tmp/* /usr/share/doc/*

# Install Packages.
RUN pip3 install requests \
    && pip3 install bs4

#run container with it mode & run python3 vulnx.py -u ...