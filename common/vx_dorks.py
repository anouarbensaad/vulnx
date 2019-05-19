import requests
import re
B = '\033[1;3;94m' #blue
W = '\033[1;97m'  # white
G = '\033[1;3;92m' # green
R = '\033[1;3;91m' # red
headers = {
        'Host' : 'bing.com',
        'User-Agent' : 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Accept': 'text/html,application/html+xml,q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

wp_contentdorks = {
        'blaze'             : 'inurl:"/wp-content/plugins/blaze-slide-show-for-wordpress/"',
        'catpro'            : 'inurl:"/wp-content/plugins/wp-catpro/"',
        'cherry'            : 'inurl:"/wp-content/plugins/cherry-plugin/"',
        'dm'                : 'inurl:"/wp-content/plugins/downloads-manager/"',
        'fromcraft'         : 'inurl:"/wp-content/plugins/formcraft/file-upload/"',
        'synoptic'          : 'inurl:"/wp-content/themes/synoptic/lib/avatarupload"',
        'shop'              : 'inurl:"/wp-content/plugins/wpshop/includes/"',
        'revslider'         : 'inurl "/wp-content/plugins/revslider/"',
        'adsmanager'        : 'inurl:"/wp-content/plugins/simple-ads-manager/"',
        'inboundiomarketing': 'inurl:"/wp-content/plugins/inboundio-marketing/"',
}
wp_admindorks = {
        'wysija'            : 'inurl":/wp-admin/admin-post.php?page=wysija_campaigns"',
        'powerzoomer'       : 'inurl:"/wp-admin/admin.php?page=powerzoomer_manage"',
        'showbiz'           : 'inurl:"/wp-admin/admin-ajax.php"',
}
wpajx = {
        'jobmanager'        : 'inurl:"/jm-ajax/upload_file/"',
}
wpindex = {
        'injection'         : 'inurl:"/index.php/wp-json/wp/"',
}
joomla = {
        'comjce'            : 'inurl":index.php?option=com_jce"'
}

def getdorksbyname(exploitname):
        if exploitname in wp_contentdorks:
                return wp_contentdorks[exploitname]
        elif exploitname in wp_admindorks:
                return wp_admindorks[exploitname]
        elif exploitname in wpajx:
                return wpajx[exploitname]
        elif exploitname in wpindex:
                return wpindex[exploitname]
        elif exploitname in joomla:
                return joomla[exploitname]
def searchengine(exploitname):
        webs = []
        bingquery = 'https://www.google.com/search?q=' + getdorksbyname(exploitname)
        res = requests.get(bingquery,headers).text
        if exploitname in wp_contentdorks:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-content/plugins/\w+'),res)
                for web in dorks:
                        if web not in webs:
                                webs.append(web)
                                print ('%s [+] URL FOUND : %s %s' %(G," \n [+] URL FOUND : ".join(webs),W))
        elif exploitname in wp_admindorks:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-admin/\w+'),res)
                for web in dorks:
                        if web not in webs:
                                webs.append(web)
                                print ('%s [+] URL FOUND : %s %s' %(G," \n [+] URL FOUND : ".join(webs),W))
        elif exploitname in wpajx:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/jm-ajax/upload_file/'),res)
                for web in dorks:
                        if web not in webs:
                                webs.append(web)
                                print ('%s [+] URL FOUND : %s %s' %(G," \n [+] URL FOUND : ".join(webs),W))
        elif exploitname in wpindex:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php/wp-json/wp/'),res)
                for web in dorks:
                        if web not in webs:
                                webs.append(web)
                                print ('%s [+] URL FOUND : %s %s' %(G," \n [+] URL FOUND : ".join(webs),W))
        elif exploitname in joomla:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php?option=com_jce'),res)
                for web in dorks:
                        if web not in webs:
                                webs.append(web)
                                print ('%s [+] URL FOUND : %s %s' %(G," \n [+] URL FOUND : ".join(webs),W))
        else:
                print('%s [-] NO URL FOUND' %(R))

searchengine('showbiz')
