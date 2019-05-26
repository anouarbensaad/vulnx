FROM python:3-alpine
#Image Labels.
LABEL name vulnx
LABEL src "https://github.com/anouarbensaad/vulnx"
LABEL creator anouarbensaad
LABEL desc "Vulnx is a cms and vulnerabilites detection, an intelligent auto shell injector,\
            fast cms detection of target and fast scanner and informations gathering like subdomains, ipaddresses, country, org, timezone, region, ans and more ...\
            Instead of injecting shell and checking it works like all the other tools do,\
            vulnx analyses the response with and recieve if shell success uploaded or no. vulnx is searching for urls with dorks."
#Clonning From Github & Install Packages.
RUN apk add git && git clone https://github.com/anouarbensaad/vulnx.git
WORKDIR vulnx
RUN pip install --upgrade pip \
	&& pip install -r ./pip/requirements.txt
#Volume vulnx mount inside the container. 
VOLUME [ "/vulnx" ]
#Entrypoint While Starting he container.
ENTRYPOINT [ "python", "vulnx.py" ]
#Default Commande.
CMD ["--help"]