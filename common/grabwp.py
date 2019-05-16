
import re
import requests
from common.colors import B,W

def wp_version(url,headers):

    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url
    response = requests.get(ep,headers)
    regexv1 = 'content=\"WordPress \d{0,9}.\d{0,9}.\d{0,9}\"'
    regexv1 = re.compile(regexv1)
    content = 'content=\"WordPress '
    endcontent = '\"$'
    matches = regexv1.findall(response.text)
    if matches and len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        sub1 = re.sub(content,'',version)
        sub2 = re.sub (endcontent,'',sub1)
        return print ('%s [*] Version : %s %s' %(B,sub2,W))

def wp_themes(url,headers):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url
    response = requests.get(ep,headers)
    regexv1 = 'themes/(.+?)/'
    regexv1 = re.compile(regexv1)
    matches = regexv1.findall(response.text)
    if matches and len(matches) > 0 and matches[0] != None and matches[0] != "":
        Theme = matches[0]
        return print ('%s [*] Themes : %s %s' %(B,Theme,W))


def wp_user(url,headers):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url + '/?author=1'
    response = requests.get(ep,headers)
    regexv1 = 'author/(.+?)/'
    regexv1 = re.compile(regexv1)
    matches = regexv1.findall(response.text)
    if matches and len(matches) > 0 and matches[0] != None and matches[0] != "":
        User = matches[0]
        return print ('%s [*] User : %s %s' %(B,User,W))
        
def wp_plugin(url,headers):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    plugins_array = []
    ep = url
    id=1
    getplugin = requests.get(ep,headers)
    regexv1 = r'wp-content/plugins/(.+?)/'
    regexv1 = re.compile(regexv1)
    matches = regexv1.findall(getplugin.text)
    for plug in matches:
        if plug not in plugins_array:
            plugins_array.append(plug)
    print ('%s [*] Plugins : %s %s' %(B," \n [*] Plugins : ".join(plugins_array),W))
