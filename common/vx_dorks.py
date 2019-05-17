import requests
import re
B = '\033[1;3;94m' #blue
W = '\033[1;97m'  # white
headers = {
        'Host' : 'bing.com',
        'User-Agent' : 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Accept': 'text/html,application/html+xml,q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }


wpdorks = {
        'wysija'            : 'inurl":/wp-admin/admin-post.php?page=wysija_campaigns"',
        'blaze'             : 'inurl:"/wp-content/plugins/blaze-slide-show-for-wordpress/"',
        'catpro'            : 'inurl:"/wp-content/plugins/wp-catpro/"',
        'cherry'            : 'inurl:"/wp-content/plugins/cherry-plugin/"',
        'dm'                : 'inurl:"/wp-content/plugins/downloads-manager/"',
        'fromcraft'         : 'inurl:"/wp-content/plugins/formcraft/file-upload/"',
        'jobmanager'        : 'inurl:"/jm-ajax/upload_file/"',
        'showbiz'           : 'inurl:"/wp-admin/admin-ajax.php"',
        'synoptic'          : 'inurl:"/wp-content/themes/synoptic/lib/avatarupload"',
        'shop'              : 'inurl:"/wp-content/plugins/wpshop/includes/"',
        'injection'         : 'inurl:"/index.php/wp-json/wp/"',
        'powerzoomer'       : 'inurl:"/wp-admin/admin.php?page=powerzoomer_manage"',
        'revslider'         : 'inurl "/wp-content/plugins/revslider/"',
        'adsmanager'        : 'inurl:"/wp-content/plugins/simple-ads-manager/"',
        'inboundiomarketing': 'inurl:"/wp-content/plugins/inboundio-marketing/"',
}

def getdorksbyname(xname):
    if xname in wpdorks:
        return wpdorks[xname]

def searchengine(xname):
    webs = []
    bingquery = 'https://www.google.com/search?q=' + getdorksbyname(xname)
    res = requests.get(bingquery,headers).text
    dorks = re.findall(re.compile(r'........./wp-content/plugins/+?'),res)
    for plug in dorks:
        if plug not in webs:
            webs.append(plug)
            print ('%s [*] Plugins : %s %s' %(B," \n [*] Plugins : ".join(webs),W))


searchengine('revslider')