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

from common.colors import red, green, bg, B, R, W, Y, G
from common.banner import banner
from common.uri_converter import convert_uri as hostd
from common.vxrequest import random_UserAgent
from common.vxrequest import getrequest as vxget
from common.grabwp import (wp_version,wp_plugin,wp_themes,wp_user)
from common.vx_dorks import (searchengine,getdorksbyname,wp_contentdorks)
from common.wp_exploits import(   wp_wysija,
                                  wp_blaze,
                                  wp_catpro,
                                  wp_cherry,
                                  wp_dm,
                                  wp_fromcraft,
                                  wp_jobmanager,
                                  wp_showbiz,
                                  wp_synoptic,
                                  wp_shop,
                                  wp_injection,
                                  wp_powerzoomer,
                                  wp_revslider,
                                  wp_adsmanager,
                                  wp_inboundiomarketing,
                                  wp_levoslideshow,
                                  wp_adblockblocker,
                                )
from common.joomla_exploits import(joomla_comjce)
#cleaning screen

def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-u', '--url', help="Url scanned for")
    parser.add_argument('-D', '--dorks', help='searching dorks', dest='dorks')
    parser.add_argument('-e', '--exploit', help='run exploit', dest='exploit')
    parser.add_argument('-f', '--file', help='Insert your file to scanning for',required=False)
    return parser.parse_args()

#args declaration
args = parse_args()
#url arg
url = args.url
#dorks arg
dorks = args.dorks
#run exploit
exploit = args.exploit

#default headers.
headers = {
#        'Host' : hostd(url),
        'User-Agent' : random_UserAgent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
# Disable SSL related warnings
warnings.filterwarnings('ignore')

def detect_cms():
    id = 0
    try:
        content=vxget(url,headers)
        #joomla searching content to detect.
        if  re.search(re.compile(r'com_content | Joomla!'), content):
            print ('%s[%i] Target -> %s %s CMS : Joomla \n\n%s' % (W,id,url,G,W))
            print ('%s [~] Check Vulnerability %s' %(Y,W))
            #joomla_exploits imported from folder[./common/joomla_exploits.py]
            joomla_comjce(url,headers)
        #prestashop searching content to detect.
        elif re.search(re.compile(r'prestashop'), content):
            print ('%s[%i] %s %s CMS : Prestashop \n\n%s' % (W,id,url,G,W))
            prestashop_version()
            domain_info()
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        #wordpress searching content to detect.
        elif re.search(re.compile(r'xmlrpc.php|wp-content|wordpress'), content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,W))
            print ('%s [+] CMS : Wordpress%s' % (G,W))
            webhosting_info()
            domain_info()
            print ('%s [~] CMS Gathering %s' %(Y,W))
            #wp_grab methods info from (folder)[./common/grapwp.py]
            wp_version(url,headers)
            wp_themes(url,headers)
            wp_user(url,headers)
            wp_plugin(url,headers)
            
            # vulnx -u http://example.com -e run | vulnx -u http://example --exploit run
            if exploit == "run":
                print ('%s [~] Check Vulnerability %s' %(Y,W))
                #wp_exploit methods from (dolder)[./common/wp_exploits.py]
                wp_wysija(url,headers)
                wp_blaze(url,headers)
                wp_catpro(url,headers)
                wp_cherry(url,headers)
                wp_dm(url,headers)
                wp_fromcraft(url,headers)
                wp_jobmanager(url,headers)
                wp_showbiz(url,headers)
                wp_synoptic(url,headers)
                wp_shop(url,headers)
                wp_injection(url,headers)
                wp_powerzoomer(url,headers)
                wp_revslider(url,headers)
                wp_adsmanager(url,headers)
                wp_inboundiomarketing(url,headers)
                wp_adblockblocker(url,headers)
                wp_levoslideshow(url,headers)

        #Drupal searching content to detect.
        elif re.search(re.compile(r'Drupal|drupal|sites/all|drupal.org'), content):
            print ('%s Target[%i] -> %s %s\n\n '% (W,id,url,W))
            print ('%s [+] CMS : Drupal%s' % (G,W))
            drupal_version()
            domain_info()
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        else:
            print ('%s[%i] %s %s CMS : Unknown \n\n%s' % (W,id,url,G,W))
            webhosting_info()
            domain_info()
    except Exception as e:
        print ('%s\n\n error : %s%s' % (R,e,W))

# drupal Version
def drupal_version():
    response = vxget(url,headers,3)
    regex = 'Drupal \d{0,10}'
    regex = re.compile(regex)
    matches = regex.findall(response)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        print ('%s [*] Drupal Version : %s %s' %(B,version,W))

# Prestashop Version
def prestashop_version():
    response = vxget(url,headers,3)
    regex = 'Prestashop \d{0,9}'
    regex = re.compile(regex)
    matches = regex.findall(response.text)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        return print ('%s [*] Prestashop Version : %s %s' %(B,version,W))

# scan domain info
def domain_info():
    print ('%s [~] Search for SubDomains %s' %(Y,W))
    searchurl = "https://www.pagesinventory.com/search/?s=" + url
    getinfo = vxget(searchurl,headers,3)
    domains = []
    #searching domain from pages inventory
    matches_domain = re.findall(re.compile(r'<td><a href=\"\/domain\/(.*?).html\">'),getinfo)
    match_ip = re.findall(re.compile(r'<a href=\"/ip\/(.*?).html\">'),getinfo)
    for domain in matches_domain:
        if domain not in domains:
            domains.append(domain)
    print ('%s [*] SubDomains : %s %s' %(B," \n [*] SubDomains : ".join(domains),W))
    if match_ip and len(match_ip) > 0 and match_ip[0] != None and match_ip[0] != "":
        IP = match_ip[0]
        print ('%s [*] IP : %s %s' %(B,IP,W))

# Web Hosting Information
def webhosting_info():
    print ('%s [~] Web Hosting Information %s' %(Y,W))
    urldate = "https://input.payapi.io/v1/api/fraud/domain/age/" + hostd(url)
    getinfo = vxget(urldate,headers,3)
    regex_date = r'Date: (.+?)-(.+?)'
    regex_date = re.compile(regex_date)
    matches = re.search(regex_date,getinfo)
    if matches:
        print ( '%s [*] Domain Created on : %s' % (B,matches.group(1)))
    ip = socket.gethostbyname(hostd(url))
    print ( '%s [*] CloudFlare IP : %s' % (B,ip))
    ipinfo = "http://ipinfo.io/" + ip + "/json"
    getipinfo = vxget(ipinfo,headers,3)
    country = re.search(re.compile(r'country\": \"(.+?)\"'),getipinfo)
    region = re.search(re.compile(r'region\": \"(.+?)\"'),getipinfo)
    if country:
        print('%s [*] Country : %s' % (B,country.group(1)))
    if region:
        print('%s [*] Region : %s' % (B,region.group(1)))
#clean
def signal_handler(signal,frame):
    print("%s(ID: {}) Cleaning up...\n Exiting...".format(signal)%(W))
    exit(0)
signal.signal(signal.SIGINT, signal_handler)

#dorks table viewing


#main
if __name__ == "__main__":
    banner()
detect_cms()
