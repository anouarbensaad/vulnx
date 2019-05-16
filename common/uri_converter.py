import sys
import re

def convert_uri(url):
    http = '^http://www.'
    https= '^https://www.'
    httpw= '^http://'
    httpsw= '^https://'
    check_httpw = re.findall(httpw,url)
    check_httpsw= re.findall(httpsw,url)
    check_http = re.findall(http,url)
    check_https= re.findall(https,url)
    if check_http:
        regex = re.compile(http)
        domain = re.sub(regex,'',url)
        return domain
    elif check_https:
        regex = re.compile(https)
        domain = re.sub(regex,'',url)
        return domain
    elif check_httpw:
        regex = re.compile(httpw)
        domain = re.sub(regex,'',url)
        return domain
    elif check_httpsw:
        regex = re.compile(httpsw)
        domain = re.sub(regex,'',url)
        return domain
