import sys
import re

def rmre(regex,url):
    compiling = re.compile(regex)
    remove_re = re.sub(compiling,'',url)
    return remove_re

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
        return rmre(http,url)
    elif check_https:
        return rmre(https,url)
    elif check_httpw:
        return rmre(httpw,url)
    elif check_httpsw:
        return rmre(httpsw,url)