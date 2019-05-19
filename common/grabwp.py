""" WordPress Information Gathering """
import re
import requests
from common.colors import B,W

#searching for the wordpress version
def wp_version(url,headers):
    ep = url
    getversion = requests.get(ep,headers).text
    #searching version content from the http response. \d{:digit} version form 0.0.0
    matches = re.search(re.compile(r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'),getversion)
    if matches:
        version = matches.group(1)
        return print ('%s [*] Version : %s %s' %(B,version,W))

#searching for the wordpress themes
def wp_themes(url,headers):
    ep = url
    themes_array = []
    getthemes = requests.get(ep,headers).text
    matches = re.findall(re.compile(r'themes/(\w+)?/'),getthemes)
    #loop for matching themes.
    for theme in matches:
        if theme not in themes_array:
            themes_array.append(theme)
    print ('%s [*] Themes : %s %s' %(B," \n [*] Themes : ".join(themes_array),W))

#searching for the wordpress user
def wp_user(url,headers):
    ep = url + '/?author=1'
    getuser = requests.get(ep,headers).text
    matches = re.search(re.compile(r'author/(\w+)?/'),getuser)
    if matches:
        user = matches.group(1)
        return print ('%s [*] User : %s %s' %(B,user,W))

#searching for the wordpress plugins
def wp_plugin(url,headers):
    plugins_array = []
    ep = url
    getplugin = requests.get(ep,headers).text
    matches = re.findall(re.compile(r'wp-content/plugins/(\w+)?/'),getplugin)
    for plug in matches:
        if plug not in plugins_array:
            plugins_array.append(plug)
    print ('%s [*] Plugins : %s %s' %(B," \n [*] Plugins : ".join(plugins_array),W))
