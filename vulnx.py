#!/usr/bin/env python
# Title : vulnx
# Author: anouarbensaad
# Desc  : CMS-Detector and Vulnerability Scanner & exploiter
"""The vulnx main part."""

import sys
import argparse
import re
import os
import socket
import common
import warnings
import signal
import requests
from common.threading import threads

##### COMMON

#colors Module.
from common.colors import red, green, bg, G, R, W, Y, G , good , bad , run , info , end , que ,bannerblue2
#banner module.
from common.banner import banner
#import parse url_convert url to domain_name.
from common.uriParser import parsing_url as hostd
#import vulnx_request::MODULE
from common.requestUp import random_UserAgent
from common.output_wr import writelogs as outlogs

##### MODULES

#import ports_scan bootcode.
from modules.portChecker import portscan
#wp cms informations
from modules.wpGrabber import (wp_version,wp_plugin,wp_themes,wp_user)
#joomla cms informations
from modules.jooGrabber import (joo_version,joo_user,joo_template)
#dnsdumpster informations gathering
from modules.dnsLookup import dnsdumper , domain_info
#import wordpress_exploits
from modules.wpExploits import(   wp_wysija,
                                  wp_blaze,
                                  wp_catpro,
                                  wp_cherry,
                                  wp_dm,
                                  wp_fromcraft,
                                  wp_jobmanager,
                                  wp_showbiz,
                                  wp_synoptic,
                                  wp_shop,
                                  wp_powerzoomer,
                                  wp_revslider,
                                  wp_adsmanager,
                                  wp_inboundiomarketing,
                                  wp_levoslideshow,
                                  wp_adblockblocker,
                                )
from modules.jooExploits import(joomla_comjce,
                                  joomla_comedia,
                                  joomla_comjdownloads,
                                  joomla_comjdownloads2,
                                  joomla_fabrik2,
                                  joomla_fabrik2_d,
                                  joomla_foxcontact,
                                )
from modules.prestaExploits import (
                                  columnadverts,
                                  soopabanners,
                                  vtslide,
                                  simpleslideshow,
                                  productpageadverts,
                                  productpageadvertsb,
                                  jro_homepageadvertise,
                                  attributewizardpro,
)

#cleaning screen

banner()

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
    parser.error = parser_error
    parser._optionals.title = "\nOPTIONS"
    parser.add_argument('-u', '--url', help="url target to scan")
    parser.add_argument('-D', '--dorks', help='search webs with dorks', dest='dorks' , type=str)
    parser.add_argument('-o', '--output', help='specify output directory',required=False)
    parser.add_argument('-t', '--timeout', help='http requests timeout', dest='timeout',type=float)
    parser.add_argument('-c', '--cms-info', help='search cms info[themes,plugins,user,version..]', dest='cms', choices=['user', 'themes','version','plugins','all'])
    parser.add_argument('--threads', help="number of threads", dest='numthread', type=float)
    parser.add_argument('-n', '--number-pages', help='search dorks number page limit', dest='numberpage' , type=int)
    parser.add_argument('-i', '--input', help='specify input file of domains to scan',dest='input_file' ,required=False)
    #Switches
    parser.add_argument('-e','--exploit', help='searching vulnerability & run exploits',
    dest='exploit', action='store_true')
    parser.add_argument('-p',  '--ports', help='ports to scan',
    dest='scanports', action='store_true')
    parser.add_argument('-w','--web-info', help='web informations gathering',
    dest='webinfo', action='store_true')
    parser.add_argument('-d','--domain-info', help='subdomains informations gathering',
    dest='domaininfo', action='store_true')
    parser.add_argument('--dns', help='dns informations gatherings',
    dest='dnsdump', action='store_true')
    parser.add_argument('-l','--dork-list', help='list names of dorks exploits',
    dest='dorkslist', action='store_true')
    return parser.parse_args()

vulnresults = set()  # results of vulnerability exploits. [success or failed]
grabinfo = set()  # return cms_detected the version , themes , plugins , user .. 
subdomains = set() # return subdomains & ip.
hostinfo = set() # host info
#args declaration
args = parse_args()
#url arg
url = args.url
#dorks arg
dorks = args.dorks
#run exploit
exploit = args.exploit
#cms gathering args
cms = args.cms
# web hosting info
webinfo = args.webinfo
# domain info
domaininfo = args.domaininfo
# dorks search.
dorks = args.dorks
dorkslist = args.dorkslist
# timeout
timeout = args.timeout or 3
#thread
numthread = args.numthread or 1
#numberpage
numberpage = args.numberpage or 1   
#portscan
scanports = args.scanports
#dns
dnsdump = args.dnsdump
#input_file
input_file = args.input_file
# Disable SSL related warnings
warnings.filterwarnings('ignore')

#method for cms detection
def detect_cms():
    lm = url + '/smiley/1.gif'
    lm_content = requests.get(lm,headers).text
    lm2 = url + '/rss.xml'
    lm2_content = requests.get(lm2,headers).text
    content=requests.get(url,headers).text
#    try:

        ############################
        #                          #
        #         joomla           #
        #                          #
        ############################
    #joomla searching content to detect.
    if  re.search(re.compile(r'<script type=\"text/javascript\" src=\"/media/system/js/mootools.js\"></script>|/media/system/js/|com_content|Joomla!'), content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s %sCMS :%s Joomla' % (good,W,end))
        print ('------------------------------------------------')
        #webinfo gathering argument
        if webinfo:
            webhosting_info(hostinfo)
        
        #domain gatherinargument
        if domaininfo:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        
        if cms == 'version':
            print (' %s CMS informations gathering' %(run))
            joo_version(url,headers)
            print ("-----------------------------------------------")
        if cms == 'all':
            print (' %s CMS informations gathering' %(run))
            joo_version(url,headers)
            joo_user(url,headers)
            joo_template(url,headers)
            print ("-----------------------------------------------")
        #port to scan
        if scanports:
            print (' %s Scanning Ports' %(run))
            print (""" %s     PORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        #joomla_exploits imported from folder[./common/joomla_exploits.py]
        if exploit:
            print (' %s Check Vulnerability' %(run))
            print (""" %sNAME                      %sSTATUS  %sSHELL"""%(W,W,W))
            joomla_comjce(url,headers,timeout)
            joomla_comedia(url,headers,timeout)
            joomla_comjdownloads(url,headers,timeout)
            joomla_comjdownloads2(url,headers,timeout)
            joomla_fabrik2(url,headers,timeout)
            joomla_fabrik2_d(url,headers,timeout)
            joomla_foxcontact(url,headers,timeout)

        ############################
        #                          #
        #         Wordpress        #
        #                          #
        ############################
    #wordpress searching content to detect.
    elif re.search(re.compile(r'wp-content|wordpress|xmlrpc.php'), content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s %sCMS :%s Wordpress' % (good,W,end))
        print ('------------------------------------------------')
        if webinfo:
            webhosting_info(hostinfo)
        if domaininfo:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        #wp_grab methods info from (folder)[./common/grapwp.py]
        if cms == 'version':
            print (' %s CMS informations gathering' %(run))
            wp_version(url,headers,grabinfo)
            print ("-----------------------------------------------")
        if cms == 'themes':
            print (' %s CMS informations gathering' %(run))
            wp_themes(url,headers,grabinfo)
            print ("-----------------------------------------------")
        if cms == 'user':
            print (' %s CMS informations gathering' %(run))
            wp_user(url,headers,grabinfo)
            print ("-----------------------------------------------")
        if cms == 'plugins':
            print (' %s CMS informations gathering' %(run))
            wp_plugin(url,headers,grabinfo)
            print ("-----------------------------------------------")
        if cms == 'all':
            print (' %s CMS informations gathering' %(run))
            wp_version(url,headers,grabinfo)
            wp_themes(url,headers,grabinfo)
            wp_user(url,headers,grabinfo)
            wp_plugin(url,headers,grabinfo)
            print ("-----------------------------------------------")
                #port to scan
        if scanports:
            print (' %s Scanning Ports' %(run))
            print (""" %sPORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        # vulnx -u http://example.com -e | vulnx -u http://example --exploit
        if exploit:
            print (' %s Check Vulnerability\n' %(run))
            print (""" %sNAME                      %sSTATUS  %sSHELL"""%(W,W,W))
            #wp_exploit methods from (dolder)[./common/wp_exploits.py]
            wp_wysija(url,headers,vulnresults)
            wp_blaze(url,headers,vulnresults)
            wp_synoptic(url,headers,vulnresults)
            wp_catpro(url,headers,vulnresults)
            wp_cherry(url,headers,vulnresults)
            wp_dm(url,headers,vulnresults)
            wp_fromcraft(url,headers,vulnresults)
            wp_jobmanager(url,headers,vulnresults)
            wp_showbiz(url,headers,vulnresults)      
            wp_shop(url,headers,vulnresults)
            wp_powerzoomer(url,headers,vulnresults)
            wp_revslider(url,headers,vulnresults)
            wp_adsmanager(url,headers,vulnresults)
            wp_inboundiomarketing(url,headers,vulnresults)
            wp_adblockblocker(url,headers,vulnresults)
            wp_levoslideshow(url,headers,vulnresults)
            print ("-----------------------------------------------")

        ############################
        #                          #
        #          Drupal          #
        #                          #
        ############################
    #drupal searching content to detect.
    elif re.search(re.compile(r'Drupal|drupal|sites/all|drupal.org'), content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s CMS : Drupal' % (good))
        print ('------------------------------------------------')
        if webinfo:
            webhosting_info(hostinfo)
        #domain gatherinargument
        if domaininfo:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        if cms == 'version':
            print (' %s CMS informations gathering' %(run))
            drupal_version()
        if scanports:
            print (' %s Scanning Ports\n' %(run))
            print (""" %s     PORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump ' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        if exploit:
            print (' %s Check Vulnerability\n' %(run))
            print (""" %sNAME                      %sSTATUS  %sSHELL"""%(W,W,W))

        ############################
        #                          #
        #        Prestashop        #
        #                          #
        ############################
    #prestashop searching content to detect.
    elif re.search(re.compile(r'Prestashop|prestashop'), content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s %sCMS :%s Prestashop' % (good,W,end))
        print ('------------------------------------------------')
        if webinfo:
            webhosting_info(hostinfo)
        #domain gatherinargument
        if domaininfo:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        if cms == 'version':
            print (' %s CMS informations gathering' %(run))
            prestashop_version()
        if scanports:
            print (' %s Scanning Ports\n' %(run))
            print (""" %s     PORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump ' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        if exploit:
            print (' %s Check Vulnerability\n' %(run))
            print (""" %sNAME                      %sSTATUS  %sSHELL"""%(W,W,W))
            columnadverts(url,headers)
            soopabanners(url,headers)
            vtslide(url,headers)
            simpleslideshow(url,headers)
            productpageadverts(url,headers)
            productpageadvertsb(url,headers)
            jro_homepageadvertise(url,headers)
            attributewizardpro(url,headers)

        ############################
        #                          #
        #          OpenCart        #
        #                          #
        ############################
    #opencart searching content to detect.
    elif re.search(re.compile(r'route=product|OpenCart|route=common|catalog/view/theme'), content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s CMS : OpenCart' % (good))
        print ('------------------------------------------------')
        if webinfo:
            webhosting_info(hostinfo)
        #domain gatherinargument
        if domaininfo:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        if cms == 'version':
            print (' %s CMS informations gathering' %(run))
        if scanports:
            print (' %s Scanning Ports\n' %(run))
            print (""" %s     PORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump ' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        if exploit:
            print (' %s Check Vulnerability\n' %(run))
            print (""" %sNAME                      %sSTATUS  %sSHELL"""%(W,W,W))

        ############################
        #                          #
        #          Magento         #
        #                          #
        ############################
    #magento searching content to detect.
    elif re.search(re.compile(r'Log into Magento Admin Page|name=\"dummy\" id=\"dummy\"|Magento'), content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s CMS : Magento' % (good))
        print ('------------------------------------------------')
        if webinfo:
            webhosting_info(hostinfo)
        #domain gatherinargument
        if domaininfo:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        if cms == 'version':
            print (' %s CMS informations gathering' %(run))
        if scanports:
            print (' %s Scanning Ports\n' %(run))
            print (""" %s     PORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump ' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        if exploit:
            print (' %s Check Vulnerability' %(run))
            print (""" %sNAME                      %sSTATUS  %sSHELL"""%(W,W,W))

        ############################
        #                          #
        #         Lokomedia        #
        #                          #
        ############################
    #lokomedia searching content to detect.
        print (' %s Check Vulnerability' %(run))
    elif re.search(re.compile(r'image/gif'), lm_content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s CMS : Lokomedia' % (good))
        print ('------------------------------------------------')
        if subdomains:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        print ('------------------------------------------------')
        if scanports:
            print (' %s Scanning Ports\n' %(run))
            print (""" %s  PORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump ' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        print (' %s Check Vulnerability' %(run))
    elif re.search(re.compile(r'lokomedia'), lm2_content):
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s CMS : Lokomedia' % (good))
        print ('------------------------------------------------')
        if subdomains:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
        if scanports:
            print (' %s Scanning Ports\n' %(run))
            print (""" %s  PORTS                     %sSTATUS  %sPROTO"""%(W,W,W))
            portscan(hostd(url))
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump ' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
        print (' %s Check Vulnerability' %(run))

        ############################
        #                          #
        #          Unknown         #
        #                          #
        ############################
    #no cms detect
    else:
        print ('\n %s[%sTarget%s]%s => %s%s \n '% (bannerblue2,W,bannerblue2, W, url, end))
        print ('------------------------------------------------')
        print (' %s looking for cms' % (que))
        print (' %s CMS : Unknown' % (bad))
        print ('------------------------------------------------')
        if webinfo:
            webhosting_info(hostinfo)
        #domain gatherinargument
        if domaininfo:
            print (' %s Starting searching for Subdomains' %(run))
            domain_info(url)
            print ("-----------------------------------------------")
        if dnsdump:
            print (' %s Starting DNS dump ' %(run))
            dnsdumper(url)
            print ("-----------------------------------------------")
#    except Exception as e:
#        print ('%s\n\n error : %s%s' % (R,e,W))

# drupal Version
def drupal_version():
    response = requests.get(url,headers).text
    regex = 'Drupal \d{0,10}'
    regex = re.compile(regex)
    matches = regex.findall(response)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        print ('%s [+] Drupal Version : %s %s' %(G,version,W))

# Prestashop Version
def prestashop_version():
    response = requests.get(url,headers).text
    regex = 'Prestashop \d{0,9}'
    regex = re.compile(regex)
    try:
      matches = regex.findall(response.text)
      if len(matches) > 0 and matches[0] != None and matches[0] != "":
          version = matches[0]
          return print ('%s [+] Prestashop Version : %s %s' %(G,version,W))
    except Exception as error_:
      print('Handling Error : '+ str(error_))

# Web Hosting Information
def webhosting_info(hostinfo):
    print (' %s Web Hosting Information' % (run))
    urldate = "https://input.payapi.io/v1/api/fraud/domain/age/" + hostd(url)
    getinfo = requests.get(urldate,headers).text
    regex_date = r'Date: (.+?)-(.+?)'
    regex_date = re.compile(regex_date)
    matches = re.search(regex_date,getinfo)
    if matches:
        print ( ' %s Domain Created on : %s' % (good,matches.group(1)))
    try:
        ip = socket.gethostbyname(hostd(url))
        print ( ' %s CloudFlare IP : %s' % (good,ip))
        ipinfo = "http://ipinfo.io/" + ip + "/json"
        getipinfo = requests.get(ipinfo,headers).text
        country = re.search(re.compile(r'country\": \"(.+?)\"'),getipinfo)
        region = re.search(re.compile(r'region\": \"(.+?)\"'),getipinfo)
        latitude = re.search(re.compile(r'latitude: (.+?)'),getipinfo)
        longitude = re.search(re.compile(r'longitude\": \"(.+?)\"'),getipinfo)
        timezone = re.search(re.compile(r'timezone\": \"(.+?)\"'),getipinfo)
        ans = re.search(re.compile(r'ans\": \"(.+?)\"'),getipinfo)
        org = re.search(re.compile(r'org\": \"(.+?)\"'),getipinfo)
        if country:
            print(' %s Country : %s' % (good,country.group(1)))
        if region:
            print(' %s Region : %s' % (good,region.group(1)))
        if latitude:
            print(' %s Latitude : %s' % (good,latitude.group(1)))
        if longitude:
            print(' %s Longitude : %s' % (good,longitude.group(1)))
        if timezone:
            print(' %s Timezone : %s' % (good,timezone.group(1)))
        if ans:
            print(' %s Ans : %s' % (good,ans.group(1)))
        if org:
            print(' %s Org : %s' % (good,org.group(1)))
        print ("-----------------------------------------------")
    except Exception as converterror:
        print(' %s Error to get ip for this web ' % (bad))
# output
output_dir = args.output or 'logs'

if not os.path.exists(output_dir): # if the directory doesn't exist
    os.mkdir(output_dir) # create a new directory

data = [ vulnresults, grabinfo, subdomains , hostinfo]

data_names = ['vulnresults', 'grabinfo', 'subdomains' , 'hostinfo']
outlogs(data,data_names,output_dir)
data = {
    'vulnresults':list(vulnresults),
    'grabinfo':list(grabinfo),
    'subdomains':list(subdomains),
}

#clean  
def signal_handler(signal,frame):
    print("%s(ID: {}) Cleaning up...\n Exiting...".format(signal)%(W))
    exit(0)
signal.signal(signal.SIGINT, signal_handler)

#main
if __name__ == "__main__":
    if input_file:
        with open(input_file,'r') as urls:
            u_array = [url.strip('\n') for url in urls]
            try:
                for url in u_array:
                    root = url
                #url condition entrypoint
                    if root.startswith('http'):
                        url = root
                    else:
                        url = 'http://'+root
                    #default headers.
                    headers = {
                    'User-Agent' : random_UserAgent(),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    }
                    detect_cms()
                    urls.close()
            except Exception as error:
                print('error : '+error)

    if url:
        #url condition entrypoint
        root = url
        if root.startswith('http'):
            url = root
        else:
            url = 'http://'+root
        #default headers.
        headers = {
        'User-Agent' : random_UserAgent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        }
        detect_cms()
    if dorks:
        headers = {
        'host' : 'google.com',
        'User-Agent' : random_UserAgent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',}
        from modules.dorksEngine import (searchengine,getdorksbyname,wp_contentdorks)
        searchengine(dorks,headers,output_dir,numberpage)
    if dorkslist:
        from modules.dorkTable import dorkslist as lsdorks
        lsdorks()
