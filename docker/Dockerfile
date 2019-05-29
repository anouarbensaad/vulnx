FROM python:3-alpine
MAINTAINER BENSAAD Anouar bensaad.tig@gmail.com

# Project Informations.
LABEL name vulnx
LABEL src "https://github.com/anouarbensaad/vulnx"
LABEL creator anouarbensaad
LABEL desc "Vulnx is a cms and vulnerabilites detection, an intelligent auto shell injector,\
            fast cms detection of target and fast scanner and informations gathering like\
	    subdomains, \
	    ipaddresses,\
	    country,    \
	    org,        \
	    timezone,   \
	    region,     \
	    ans         \
	    and more ...\
            Instead of injecting shell and checking it works like all the other tools do,\
            vulnx analyses the response with and recieve if shell success uploaded or no.\
	    vulnx is searching for urls with dorks."
	    
# Clonning Vulnx From Github
RUN apk add git && \
    git clone https://github.com/anouarbensaad/vulnx.git

# Working−Directory
WORKDIR vulnx

# Install Pip Packages.
RUN pip install --upgrade pip && \
    pip install -r ./pip/requirements.txt
    
# Add Mount Volume Docker To Save All changes. 
VOLUME [ "/vulnx" ]

# Entrypoint -> Command : While Creating Container.
ENTRYPOINT [ "python", "vulnx.py" ]

# Default Command When Starting The Container.
CMD ["--help"]
