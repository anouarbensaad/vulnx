import re
from urllib.parse import urlparse


def parsing_url(url):
    host = urlparse(url).netloc
    return host
