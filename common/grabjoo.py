""" Joomla Information Gathering """
from common.colors import red, green, bg, G, R, W, Y, G , good , bad , run , info , end , que
import re
import requests
# Find Joomla version and check it on exploit-db
def joo_version(url,headers):
    endpoint = url + "/administrator/manifests/files" + '/joomla.xml'
    response = requests.get(endpoint,headers).text
    regex = r'<version>(.+?)</version>'
    pattern = re.compile(regex)
    version = re.findall(pattern, response)
    if version:
        return print (' %s Version : %s' %(good,version[0]))

def joo_user(url,headers):
    users = []
    endpoint = url + '/?format=feed'
    response = requests.get(endpoint,headers).text
    regex = r'<author>(.+?) \((.+?)\)</author>'
    pattern = re.compile(regex)
    joouser = re.findall(pattern, response)
    if joouser:
        joouser = sorted(set(joouser))
        for user in joouser:
            users.append(user[1])
            msg = user[1] + ": " + user[0]
            print(msg)
