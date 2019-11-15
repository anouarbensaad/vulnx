'''
Dorks Engine Module.
github Repository : http://github.com/anouarbensaad/findorks
'''

import requests
import re
import time
import random
import os
from common.colors import run,W,end,good,bad,que,info,bannerblue
from common.uriParser import parsing_url as parsify
filename = time.strftime("%Y-%m-%d-%H%M%S-Dorks")
output_dirdorks = 'logs'+'/Dorks'

if not os.path.exists(output_dirdorks): # if the directory doesn't exist
        os.mkdir(output_dirdorks) # create a new directory
        export = open('%s/%s.txt' % (output_dirdorks,filename),'w')
else:
        export = open('%s/%s.txt' % (output_dirdorks,filename),'w')


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
        'thumbslider'       : 'inurl:"/wp-content/plugins/wp-responsive-thumbnail-slider"',
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

prestashop = {
        'columnadverts'          : 'inurl":/modules/columnadverts/"',
        'soopabanners'           : 'inurl":/modules/soopabanners/"',
        'vtslide'                : 'inurl":/modules/soopabanners/"',
        'simpleslideshow'        : 'inurl":/modules/simpleslideshow/"',
        'productpageadverts'     : 'inurl":/modules/productpageadverts/"',
        'productpageadvertsb'    : 'inurl":/modules/homepageadvertise2/"',
        'jro_homepageadvertise'  : 'inurl":/modules/jro_homepageadvertise/"',
        'attributewizardpro'     : 'inurl":/modules/attributewizardpro/"',
        'oneattributewizardpro'  : 'inurl":/modules/1attributewizardpro/"',
        'attributewizardpro_old' : 'inurl":/modules/attributewizardpro.OLD/"',
        'attributewizardpro_x'   : 'inurl":/modules/attributewizardpro_x/"',
        'advancedslider'         : 'inurl":/modules/advancedslider/"',
        'cartabandonmentpro'     : 'inurl":/modules/cartabandonmentpro/"',
        'cartabandonmentpro_old' : 'inurl":/modules/cartabandonmentproOld/"' ,  
        'videostab'              : 'inurl":/modules/videostab/"',
        'wg24themeadministration': 'inurl":/modules//wg24themeadministration/"',
        'fieldvmegamenu'         : 'inurl":/modules/fieldvmegamenu/"',
        'wdoptionpanel'          : 'inurl":/modules/wdoptionpanel/"',
        'pk_flexmenu'            : 'inurl":/modules/pk_flexmenu/"',
        'pk_vertflexmenu'        : 'inurl":/modules/pk_vertflexmenu/"',
        'nvn_export_orders'      : 'inurl":/modules/nvn_export_orders/"',
        'tdpsthemeoptionpanel'   : 'inurl":/modules/tdpsthemeoptionpanel/"',
        'masseditproduct'        : 'inurl":/modules/lib/redactor/"',
}

class Dorks:

        @staticmethod
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
                elif exploitname in prestashop:
                        return prestashop[exploitname]
        
        @staticmethod
        def searchengine(exploitname,headers,output_dir,numberpage):
                try :
                        print (' %s Searching for %s dork url' %(run,exploitname))
                        numberpage = numberpage*10
                        for np in range(0,numberpage,10):
                                starty = time.time()
                                if np==0:
                                        time.sleep(random.randint(1,2))
                                        print(' %s Page n° 1 ' % (info))
                                        googlequery = 'https://www.google.com/search?q='+Dorks.getdorksbyname(exploitname)
                                        print(' %s searching for : %s'% (que,googlequery))
                                        res = requests.get(googlequery,headers).text
                                        if (re.findall(re.compile(r'CAPTCHA'),res)):
                                                print(' %s Bot Detected The block will expire shortly' % bad)
                                        else:
                                                Dorks.WP_dorksconditions(exploitname,res,output_dir)
                                                print ('------------------------------------------------')
                                else:
                                        time.sleep(random.randint(3,5))
                                        print(' %s Page n° %i ' % (info,np/10+1))
                                        googlequery = 'https://www.google.com/search?q='+Dorks.getdorksbyname(exploitname)+'&start='+str(np)
                                        res = requests.get(googlequery,headers).text
                                        print(' %s searching for : %s'% (que,googlequery))
                                        if (re.findall(re.compile(r'CAPTCHA'),res)):
                                                print(' %s Bot Detected The block will expire shortly' % bad)
                                        else:
                                                Dorks.WP_dorksconditions(exploitname,res,output_dir)
                                                print ('------------------------------------------------')
                                endy = time.time()
                                elapsed = endy - starty
                                print (' %s Elapsed Time : %.2f seconds' % (info,elapsed))
                                print("%s----------------%s"%(bannerblue,end))
                        export.close()
                except Exception as msg:
                        print(' %s exploitname %s ' %(bad,msg))
                np=+10

        @staticmethod
        def WP_dorksconditions(exploitname,response,output_dir):
                webs = []
                if exploitname in wp_contentdorks:
                        dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-content/plugins/\w+'),response)
                        if len(dorks) > 0:
                                for web in dorks:
                                        if web not in webs:
                                                webs.append(web)
                                for i in range(len(webs)):
                                        domains = parsify(webs[i])
                                        print (' %s URL   : %s ' %(good , webs[i]))
                                        print (' %s DOMAIN: %s ' %(good , domains))
                                        export.write(domains)
                                        export.write('\n')
                elif exploitname in wp_admindorks:      
                        dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-admin/\w+'),response)
                        if len(dorks) > 0:
                                for web in dorks:
                                        if web not in webs:
                                                webs.append(web)
                                for i in range(len(webs)):
                                        domains = parsify(webs[i])
                                        print (' %s URL   : %s ' %(good , webs[i]))
                                        print (' %s DOMAIN: %s ' %(good , domains))
                                        export.write(domains)
                                        export.write('\n')
                elif exploitname in wpajx:
                        dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/jm-ajax/upload_file/'),response)
                        if len(dorks) > 0:
                                for web in dorks:
                                        if web not in webs:
                                                webs.append(web)
                                for i in range(len(webs)):
                                        domains = parsify(webs[i])
                                        print (' %s URL   : %s ' %(good , webs[i]))
                                        print (' %s DOMAIN: %s ' %(good , domains))
                                        export.write(domains)
                                        export.write('\n')
                elif exploitname in wpindex:
                        dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php/wp-json/wp/'),response)
                        if len(dorks) > 0:
                                for web in dorks:
                                        if web not in webs:
                                                webs.append(web)
                                for i in range(len(webs)):
                                        domains = parsify(webs[i])
                                        print (' %s URL   : %s ' %(good , webs[i]))
                                        print (' %s DOMAIN: %s ' %(good , domains))
                                        export.write(domains)
                                        export.write('\n')
                elif exploitname in joomla:
                        dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php?option=com_jce'),response)
                        if len(dorks) > 0:
                                for web in dorks:
                                        if web not in webs:
                                                webs.append(web)
                                for i in range(len(webs)):
                                        domains = parsify(webs[i])
                                        print (' %s URL   : %s ' %(good , webs[i]))
                                        print (' %s DOMAIN: %s ' %(good , domains))
                                        export.write(domains)
                                        export.write('\n')
                elif exploitname in prestashop:
                        dorks = re.findall(re.compile(r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/modules/\w+'),response)
                        if len(dorks) > 0:
                                for web in dorks:
                                        if web not in webs:
                                                webs.append(web)
                                for i in range(len(webs)):
                                        domains = parsify(webs[i])
                                        print (' %s URL   : %s ' %(good , webs[i]))
                                        print (' %s DOMAIN: %s ' %(good , domains))
                                        export.write(domains)
                                        export.write('\n')

class DorkList():

        @staticmethod
        def dorkslist():
                print (" %s lists of existing dorks" % (info))
                print ("""%s
                +−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−+
                |  WordPress           |  Joomla         |  Drupal          |   Prestashop               |  Lokomedia      |
                +−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−−−−+%s
                |  blaze               |  comjce         |                  |   columnadverts            |                 |
                |  catpro              |  comfabrik      |                  |   soopabanners             |                 |
                |  cherry              |  comjdownloads  |                  |   vtslide                  |                 |
                |  dm                  |  comfoxcontact  |                  |   simpleslideshow          |                 |
                |  fromcraft           |                 |                  |   productpageadverts       |                 |
                |  synoptic            |                 |                  |   productpageadvertsb      |                 |
                |  shop                |                 |                  |   jro_homepageadvertise    |                 |
                |  revslider           |                 |                  |   attributewizardpro       |                 |
                |  adsmanager          |                 |                  |   oneattributewizardpro    |                 |
                |  inboundiomarketing  |                 |                  |   attributewizardpro_old   |                 |
                |  wysija              |                 |                  |   attributewizardpro_x     |                 |
                |  powerzoomer         |                 |                  |   advancedslider           |                 |
                |  showbiz             |                 |                  |   cartabandonmentpro       |                 |
                |  jobmanager          |                 |                  |   cartabandonmentpro_old   |                 |
                |  injection           |                 |                  |   videostab                |                 |
                |  thumbslider         |                 |                  |   wg24themeadministration  |                 |
                |                      |                 |                  |   fieldvmegamenu           |                 |
                |                      |                 |                  |   wdoptionpanel            |                 |
                |                      |                 |                  |   pk_flexmenu              |                 |
                |                      |                 |                  |   pk_vertflexmenu          |                 |
                |                      |                 |                  |   nvn_export_orders        |                 |
                |                      |                 |                  |   tdpsthemeoptionpanel     |                 |
                |                      |                 |                  |   masseditproduct          |                 |                                    
                +----------------------+-----------------+------------------+----------------------------+-----------------+
                
                """ %(W,end))
                print ('------------------------------------------------')

        @staticmethod
        def wp_dorkTable():
                print(" %s lists of wordpress dorks" % (info))
                print("""%s
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |  WordPress                 |
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |  blaze                     |
                |  catpro                    |
                |  cherry                    |
                |  dm                        |
                |  fromcraft                 |
                |  synoptic                  |
                |  shop                      |
                |  revslider                 |
                |  adsmanager                |
                |  inboundiomarketing        |
                |  wysija                    |
                |  powerzoomer               |
                |  showbiz                   |
                |  jobmanager                |
                |  injection                 |
                |  thumbslider               |
                |                            |
                +----------------------------+%s
                """%(W,end))
                print ('------------------------------------------------')

        @staticmethod
        def joo_dorkTable():
                print(" %s lists of wordpress dorks" % (info))
                print("""%s
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |  Joomla                     |
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |  comjce                     |
                |  comfabrik                  |
                |  comjdownloads              |
                |  comfoxcontact              |
                |                             |
                |                             |
                |                             |
                |                             |
                |                             |
                |                             |
                |                             |
                |                             |
                |                             |
                |                             |
                |                             |
                +----------------------------+%s
                """%(W,end))
                print ('------------------------------------------------')

        @staticmethod
        def ps_dorkTable():
                print(" %s lists of wordpress dorks" % (info))
                print("""%s
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |   Prestashop               |
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |   columnadverts            |
                |   soopabanners             |
                |   vtslide                  |
                |   simpleslideshow          |
                |   productpageadverts       |
                |   productpageadvertsb      |
                |   jro_homepageadvertise    |
                |   attributewizardpro       |
                |   oneattributewizardpro    |
                |   attributewizardpro_old   |
                |   attributewizardpro_x     |
                |   advancedslider           |
                |   cartabandonmentpro       |
                |   cartabandonmentpro_old   |
                |   videostab                |
                |   wg24themeadministration  |
                |   fieldvmegamenu           |
                |   wdoptionpanel            |
                |   pk_flexmenu              |
                |   pk_vertflexmenu          |
                |   nvn_export_orders        |
                |   tdpsthemeoptionpanel     |
                |   masseditproduct          |
                +----------------------------+%s
                """%(W,end))
                print ('------------------------------------------------')

        @staticmethod
        def loko_dorkTable():
                print(" %s lists of wordpress dorks" % (info))
                print("""%s
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |   Lokomedia                |
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                +----------------------------+%s
                """%(W,end))
                print ('------------------------------------------------')

        @staticmethod
        def dru_dorkTable():
                print(" %s lists of wordpress dorks" % (info))
                print("""%s
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |   Drupal                   |
                +−−−−−−−−−−−−−−−−−−−−−−−−−−−−+
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                |                            |
                +----------------------------+%s
                """%(W,end))
                print ('------------------------------------------------')