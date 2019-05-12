FROM python:3-alpine

LABEL name VulnX
LABEL src "https://github.com/anouarbensaad/VulnX"
LABEL creator anouarbensaad
LABEL desc "CMS-Detector and Vulnerability Scanner & exploiter"

RUN apk add git && git clone https://github.com/anouarbensaad/VulnX.git VulnX
WORKDIR VulnX
RUN pip install -r ./pip/requirements.txt

VOLUME [ "/VulnX" ]
ENTRYPOINT [ "python3", "vulnx.py" ]