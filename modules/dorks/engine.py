
#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)

'''
Dorks Engine Module.
github Repository : http://github.com/anouarbensaad/findorks
'''

import requests
import re
import time
import random
import os
from common.colors import run, W, end, good, bad, que, info, bannerblue
from common.uriParser import parsing_url as parsify
output_dirdorks = 'logs'+'/Dorks'

#if not os.path.exists(output_dirdorks):  # if the directory doesn't exist
#    os.mkdir(output_dirdorks)  # create a new directory
#    export = open('%s/%s.txt' % (output_dirdorks, filename), 'w')
#else:
#    export = open('%s/%s.txt' % (output_dirdorks, filename), 'w')


wp_contentdorks = {
    'blaze': 'inurl:"/wp-content/plugins/blaze-slide-show-for-wordpress/"',
    'catpro': 'inurl:"/wp-content/plugins/wp-catpro/"',
    'cherry': 'inurl:"/wp-content/plugins/cherry-plugin/"',
    'dm': 'inurl:"/wp-content/plugins/downloads-manager/"',
    'fromcraft': 'inurl:"/wp-content/plugins/formcraft/file-upload/"',
    'synoptic': 'inurl:"/wp-content/themes/synoptic/lib/avatarupload"',
    'shop': 'inurl:"/wp-content/plugins/wpshop/includes/"',
    'revslider': 'inurl "/wp-content/plugins/revslider/"',
    'adsmanager': 'inurl:"/wp-content/plugins/simple-ads-manager/"',
    'inboundiomarketing': 'inurl:"/wp-content/plugins/inboundio-marketing/"',
    'thumbslider': 'inurl:"/wp-content/plugins/wp-responsive-thumbnail-slider"',
}
wp_admindorks = {
    'wysija': 'inurl:"/wp-admin/admin-post.php?page=wysija_campaigns"',
    'powerzoomer': 'inurl:"/wp-admin/admin.php?page=powerzoomer_manage"',
    'showbiz': 'inurl:"/wp-admin/admin-ajax.php"',
}

wpajx = {
    'jobmanager': 'inurl:"/jm-ajax/upload_file/"',
}


wpindex = {
    'injection': 'inurl:"/index.php/wp-json/wp/"',
}


joomla = {
    'comjce': 'inurl:"index.php?option=com_jce"',
    'comfabrik': 'inurl:"index.php?option=com_fabrik"',
    'comjdownloads': 'inurl:"index.php?option=com_fabrik"',
    'comfoxcontact': 'inurl:"index.php?option=com_foxcontact"',
}

prestashop = {
    'columnadverts': 'inurl:"/modules/columnadverts/"',
    'soopabanners': 'inurl:"/modules/soopabanners/"',
    'vtslide': 'inurl:"/modules/soopabanners/"',
    'simpleslideshow': 'inurl:"/modules/simpleslideshow/"',
    'productpageadverts': 'inurl:"/modules/productpageadverts/"',
    'productpageadvertsb': 'inurl:"/modules/homepageadvertise2/"',
    'jro_homepageadvertise': 'inurl:"/modules/jro_homepageadvertise/"',
    'attributewizardpro': 'inurl:"/modules/attributewizardpro/"',
    'oneattributewizardpro': 'inurl:"/modules/1attributewizardpro/"',
    'attributewizardpro_old': 'inurl:"/modules/attributewizardpro.OLD/"',
    'attributewizardpro_x': 'inurl:"/modules/attributewizardpro_x/"',
    'advancedslider': 'inurl:"/modules/advancedslider/"',
    'cartabandonmentpro': 'inurl:"/modules/cartabandonmentpro/"',
    'cartabandonmentpro_old': 'inurl:"/modules/cartabandonmentproOld/"',
    'videostab': 'inurl:"/modules/videostab/"',
    'wg24themeadministration': 'inurl:"/modules//wg24themeadministration/"',
    'fieldvmegamenu': 'inurl:"/modules/fieldvmegamenu/"',
    'wdoptionpanel': 'inurl:"/modules/wdoptionpanel/"',
    'pk_flexmenu': 'inurl:"/modules/pk_flexmenu/"',
    'pk_vertflexmenu': 'inurl:"/modules/pk_vertflexmenu/"',
    'nvn_export_orders': 'inurl:"/modules/nvn_export_orders/"',
    'tdpsthemeoptionpanel': 'inurl:"/modules/tdpsthemeoptionpanel/"',
    'masseditproduct': 'inurl:"/modules/lib/redactor/"',
}


class Dork:

    def __init__(self,headers=None,exploit=None,pages=1):
        self.headers = headers
        self.exploit = exploit
        self.pages = pages

    def __setdork__(self):

        '''
        this method to set the right dork from the exploit name.
        '''
        if self.exploit is None:
            return dict(
                message='This exploit not valid'
            )
        else:
            if self.exploit in wp_contentdorks:
                return dict(
                    dork=wp_contentdorks[self.exploit]
                )
            if self.exploit in wp_admindorks:
                return dict(
                    dork=wp_admindorks[self.exploit]
                )
            if self.exploit in wpajx:
                return dict(
                    dork=wpajx[self.exploit]
                )
            if self.exploit in wpindex:
                return dict(
                    dork=wpindex[self.exploit]
                )
            if self.exploit in joomla:
                return dict(
                    dork=joomla[self.exploit]
                )
            if self.exploit in prestashop:
                return dict(
                    dork=prestashop[self.exploit]
                )

    def __finddork__(self,content):
        webs = []
        if self.exploit in wp_contentdorks:
            dorks = re.findall(re.compile(
                r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-content/plugins/\w+'), content)
            if len(dorks) > 0:
                for web in dorks:
                    if web not in webs:
                        webs.append(web)
                for i in range(len(webs)):
                    domains = parsify(webs[i])
                    print(' {0} URL   : {1} ' .format(good, webs[i]))
                    print(' {0} DOMAIN: {1} ' .format(good, domains))
        elif self.exploit in wp_admindorks:
            dorks = re.findall(re.compile(
                r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/wp-admin/\w+'), content)
            if len(dorks) > 0:
                for web in dorks:
                    if web not in webs:
                        webs.append(web)
                for i in range(len(webs)):
                    domains = parsify(webs[i])
                    print(' {0} URL   : {1} ' .format(good, webs[i]))
                    print(' {0} DOMAIN: {1} ' .format(good, domains))
        elif self.exploit in wpajx:
            dorks = re.findall(re.compile(
                r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/jm-ajax/upload_file/'), content)
            if len(dorks) > 0:
                for web in dorks:
                    if web not in webs:
                        webs.append(web)
                for i in range(len(webs)):
                    domains = parsify(webs[i])
                    print(' {0} URL   : {1} ' .format(good, webs[i]))
                    print(' {0} DOMAIN: {1} ' .format(good, domains))
        elif self.exploit in wpindex:
            dorks = re.findall(re.compile(
                r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php/wp-json/wp/'), content)
            if len(dorks) > 0:
                for web in dorks:
                    if web not in webs:
                        webs.append(web)
                for i in range(len(webs)):
                    domains = parsify(webs[i])
                    print(' {0} URL   : {1} ' .format(good, webs[i]))
                    print(' {0} DOMAIN: {1} ' .format(good, domains))
        elif self.exploit in joomla:
            dorks = re.findall(re.compile(
                r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/index.php?option=com_jce'), content)
            if len(dorks) > 0:
                for web in dorks:
                    if web not in webs:
                        webs.append(web)
                for i in range(len(webs)):
                    domains = parsify(webs[i])
                    print(' {0} URL   : {1} ' .format(good, webs[i]))
                    print(' {0} DOMAIN: {1} ' .format(good, domains))
        elif self.exploit in prestashop:
            dorks = re.findall(re.compile(
                r'https?://+?\w+?[a-zA-Z0-9-_.]+?[a-zA-Z0-9-_.]?\w+\.\w+/?/modules/\w+'), content)
            if len(dorks) > 0:
                for web in dorks:
                    if web not in webs:
                        webs.append(web)
                for i in range(len(webs)):
                    domains = parsify(webs[i])
                    print(' {0} URL   : {1} ' .format(good, webs[i]))
                    print(' {0} DOMAIN: {1} ' .format(good, domains))


    def detect_captcha(self,content):

        '''
        this method to detect if there is a captcha or not.
        - randomize the time of query
        - randomize the header and user-agent. to skip the detection.
        '''
        if (re.findall(re.compile(r'CAPTCHA'), content)):
            return True
        else:
            return False

    def _google_singlepage_(self):

        print(' {0} Page N° 1 '.format(info))
        set_dork = self.__setdork__()
        google_query = 'https://www.google.com/search?q=' + set_dork['dork']
        print(' {0} searching for : {1}' .format(que, google_query))
        response = requests.get(google_query,headers=self.headers).text
        return response

    def _google_multipage_(self,num_p):

        print(' {0} Page n° {1} ' .format(info, num_p/10+1))
        set_dork = self.__setdork__()
        google_query = 'https://www.google.com/search?q=' + set_dork['dork']+'&start='+str(num_p)
        print(' %s searching for : %s' % (que, google_query))
        response = requests.get(google_query, headers=self.headers).text
        return response

    def search(self):
        pages = self.pages*10
        try:
            for number_page in range(0,pages,10):
                init_time = time.time()
                if number_page == 0:
                    time.sleep(random.randint(1,2))
                    if self.detect_captcha(self._google_singlepage_()):
                        print(' {0} Bot Detected The block will expire shortly' .format(bad))
                    else:
                        self.__finddork__(self._google_singlepage_())
                else:
                    time.sleep(random.randint(3,5))
                    if self.detect_captcha(self._google_multipage_(number_page)):
                        print(' {0} Bot Detected The block will expire shortly' .format(bad))
                    else:
                        self.__finddork__(self._google_multipage_(number_page))
                end_time = time.time()
                elapsed_time = end_time - init_time
                print(' %s Elapsed Time : %.2f seconds' % (info, elapsed_time))
        except Exception as msg:
            print(' %s exploitname %s ' % (bad, msg))
        number_page = +10
