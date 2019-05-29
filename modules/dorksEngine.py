import requests
import re
import time
import random
import os
from common.colors import run,W,end,good,bad,que,info,bannerblue
from common.requestUp import getrequest as vulnxget
from common.uriParser import parsing_url as parsify
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
        'thumbslider'       :'inurl:"/wp-content/plugins/wp-responsive-thumbnail-slider"',
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
        'comjce'            : 'inurl":index.php?option=com_jce"',
        'comfabrik'         : 'inurl":index.php?option=com_fabrik"',
        'comjdownloads'     : 'inurl":index.php?option=com_fabrik"',
        'comfoxcontact'     : 'inurl":index.php?option=com_foxcontact"',
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
def searchengine(exploitname,headers,output_dir,numberpage):
        try :
                print (' %s Searching for %s dork url' %(run,exploitname))
                numberpage = numberpage*10
                for np in range(0,numberpage,10):
                        starty = time.time()
                        if np==0:
                                time.sleep(random.randint(1,2))
                                print(' %s Page n° 1 ' % (info))
                                googlequery = 'https://www.google.com/search?q='+getdorksbyname(exploitname)
                                print(' %s searching for : %s'% (que,googlequery))
                                res = requests.get(googlequery,headers).text
                                if (re.findall(re.compile(r'CAPTCHA'),res)):
                                        print(' %s Bot Detected The block will expire shortly' % bad)
                                else:
                                        WP_dorksconditions(exploitname,res,output_dir)
                                        print ('------------------------------------------------')
                        else:
                                time.sleep(random.randint(3,5))
                                print(' %s Page n° %i ' % (info,np/10+1))
                                googlequery = 'https://www.google.com/search?q='+getdorksbyname(exploitname)+'&start='+str(np)
                                res = requests.get(googlequery,headers).text
                                print(' %s searching for : %s'% (que,googlequery))
                                if (re.findall(re.compile(r'CAPTCHA'),res)):
                                        print(' %s Bot Detected The block will expire shortly' % bad)
                                else:
                                        WP_dorksconditions(exploitname,res,output_dir)
                                        print ('------------------------------------------------')
                        endy = time.time()
                        elapsed = endy - starty
                        print (' %s Elapsed Time : %.2f seconds' % (info,elapsed))
                        print("%s----------------%s"%(bannerblue,end))
        except Exception as msg:
                print(' %s exploitname %s ' %(bad,msg))
        np=+10
def WP_dorksconditions(exploitname,response,output_dir):
        filename = time.strftime("%Y-%m-%d-%H%M%S-Dorks")
        output_dirdorks = output_dir+'/Dorks'
        if not os.path.exists(output_dirdorks): # if the directory doesn't exist
                os.mkdir(output_dirdorks) # create a new directory
        webs = []
        if exploitname in wp_contentdorks:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-content/plugins/\w+'),response)
                if len(dorks) > 0:
                        export= open('%s/%s.txt' % (output_dirdorks,filename),'w')
                        for web in dorks:
                                if web not in webs:
                                        webs.append(web)
                        for i in range(len(webs)):
                                domains = parsify(webs[i])
                                print (' %s URL   : %s ' %(good , webs[i]))
                                print (' %s DOMAIN: %s ' %(good , domains))
                                export.write(domains)
                                export.write('\n')
                        export.close()
        elif exploitname in wp_admindorks:      
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-admin/\w+'),response)
                if len(dorks) > 0:
                        export= open('%s/%s.txt' % (output_dirdorks,filename),'w')
                        for web in dorks:
                                if web not in webs:
                                        webs.append(web)
                        for i in range(len(webs)):
                                domains = parsify(webs[i])
                                print (' %s URL   : %s ' %(good , webs[i]))
                                print (' %s DOMAIN: %s ' %(good , domains))
                                export.write(domains)
                                export.write('\n')
                        export.close()
        elif exploitname in wpajx:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/jm-ajax/upload_file/'),response)
                if len(dorks) > 0:
                        export= open('%s/%s.txt' % (output_dirdorks,filename),'w')
                        for web in dorks:
                                if web not in webs:
                                        webs.append(web)
                        for i in range(len(webs)):
                                domains = parsify(webs[i])
                                print (' %s URL   : %s ' %(good , webs[i]))
                                print (' %s DOMAIN: %s ' %(good , domains))
                                export.write(domains)
                                export.write('\n')
                        export.close()
        elif exploitname in wpindex:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php/wp-json/wp/'),response)
                if len(dorks) > 0:
                        export= open('%s/%s.txt' % (output_dirdorks,filename),'w')
                        for web in dorks:
                                if web not in webs:
                                        webs.append(web)
                        for i in range(len(webs)):
                                domains = parsify(webs[i])
                                print (' %s URL   : %s ' %(good , webs[i]))
                                print (' %s DOMAIN: %s ' %(good , domains))
                                export.write(domains)
                                export.write('\n')
                        export.close()
        elif exploitname in joomla:
                dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php?option=com_jce'),response)
                if len(dorks) > 0:
                        export= open('%s/%s.txt' % (output_dirdorks,filename),'w')
                        for web in dorks:
                                if web not in webs:
                                        webs.append(web)
                        for i in range(len(webs)):
                                domains = parsify(webs[i])
                                print (' %s URL   : %s ' %(good , webs[i]))
                                print (' %s DOMAIN: %s ' %(good , domains))
                                export.write(domains)
                                export.write('\n')
                        export.close()
