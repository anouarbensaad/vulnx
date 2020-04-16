""" WordPress Information Gathering """
import re
import requests
from common.colors import B, W, G, good, bad

# searching for the wordpress version


def wp_version(url, headers, grabinfo):
    ep = url
    getversion = requests.get(ep, headers).text
    # searching version content from the http response. \d{:digit} version form 0.0.0
    matches = re.search(re.compile(
        r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'), getversion)
    if matches:
        version = matches.group(1)
        return print(' %s Version : %s' % (good, version))
        grabinfo.add('Version - ' + version)
# searching for the wordpress themes


def wp_themes(url, headers, grabinfo):
    ep = url
    themes_array = []
    getthemes = requests.get(ep, headers).text
    matches = re.findall(re.compile(r'themes/(\w+)?/'), getthemes)
    # loop for matching themes.)
    if len(matches) > 0:
        for theme in matches:
            if theme not in themes_array:
                themes_array.append(theme)
        for i in range(len(themes_array)):
            print(' %s Themes : %s ' % (good, themes_array[i]))
# searching for the wordpress user


def wp_user(url, headers, grabinfo):
    ep = url + '/?author=1'
    getuser = requests.get(ep, headers).text
    matches = re.search(re.compile(r'author/(\w+)?/'), getuser)
    if matches:
        user = matches.group(1)
        return print(' %s User : %s' % (good, user))
        grabinfo.add('user - ' + user)

# searching for the wordpress plugins


def wp_plugin(url, headers, grabinfo):
    plugins_array = []
    ep = url
    getplugin = requests.get(ep, headers).text
    matches = re.findall(re.compile(r'wp-content/plugins/(\w+)?/'), getplugin)
    if len(matches) > 0:
        for plugin in matches:
            if plugin not in plugins_array:
                plugins_array.append(plugin)
        for i in range(len(plugins_array)):
            print(' %s Plugins : %s ' % (good, plugins_array[i]))
