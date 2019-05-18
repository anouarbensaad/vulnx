FROM python:3-alpine

LABEL name VulnX
LABEL src "https://github.com/anouarbensaad/VulnX"
LABEL creator anouarbensaad
LABEL desc "CMS-Detector and Vulnerability Scanner & exploiter"

RUN apk add git && git clone https://github.com/anouarbensaad/VulnX.git VulnX
WORKDIR VulnX
RUN pip install --upgrade pip ; pip install requests ;
VOLUME [ "/VulnX" ]
ENTRYPOINT [ "python", "vulnx.py" ]
CMD ["--help"]
