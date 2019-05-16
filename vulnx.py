#!/usr/bin/env python

# Title : vulnx
# Author: anouarbensaad
# Desc  : CMS-Detector and Vulnerability Scanner & exploiter

"""The vulnx main part."""

import sys
import argparse
import re
import requests
import os
import socket
import common
from common.colors import red, green, bg, B, R, W, Y, G
from common.banner import banner
from common.uri_converter import convert_uri as uconvert
from common.grabwp import wp_version, wp_plugin, wp_themes, wp_user
from common.wp_exploits import (wp_wysija,
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
                                wp_inboundiomarketing
                                )

os.system('clear')
headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31",
            "Keep-Alive": "timeout=15",
            "verify" : False
}

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
    parser.add_argument('-f', '--file', help='Insert your file to scanning for',required=False)
    return parser.parse_args()
def detect_cms():
    id = 0
    try:
        r=requests.get(url, headers)
        content = r.text
        joomla = re.search(re.compile(r'com_content | Joomla!'), content)
        wordpress = re.search(re.compile(r'xmlrpc.php|wp-content|wordpress'), content)
        drupal = re.search(re.compile(r'Drupal|drupal|sites/all|drupal.org'), content)
        prestashop = re.search(re.compile(r'prestashop'), content)
        if joomla:
            print ('%s[%i] Target -> %s %s CMS : Joomla \n\n%s' % (W,id,url,G,W))
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        elif prestashop:
            print ('%s[%i] %s %s CMS : Prestashop \n\n%s' % (W,id,url,G,W))
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        elif wordpress:
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
        elif drupal:
            print ('%s Target[%i] -> %s %s\n\n '% (W,id,url,W))
            print ('%s [+] CMS : Drupal%s' % (G,W))
            drupal_version()
            domain_info()
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        else:
            print ('%s[%i] %s %s CMS : Unknown \n\n%s' % (W,id,url,G,W))
            prestashop_version()
            domain_info()
            print ('%s [~] Check Vulnerability %s' %(Y,W))
    except Exception as e:
        print ('%s\n\nerror : %s%s' % (R,e,W))
        
# drupal Version
def drupal_version():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url
    uknownversion = "UKNOWN"
    response = requests.get(ep,headers)
    regex = 'Drupal \d{0,10}'
    regex = re.compile(regex)
    matches = regex.findall(response.text)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        return print ('%s [*] Drupal Version : %s %s' %(B,version,W))
    else:
        return print ('%s [!] Drupal Version : %s %s' %(R,uknownversion,W))

# Prestashop Version
def prestashop_version():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
    }
    ep = url
    uknownversion = "UKNOWN"
    response = requests.get(ep,headers,Verify=False)
    regex = 'Prestashop \d{0,9}'
    regex = re.compile(regex)
    matches = regex.findall(response.text)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        return print ('%s [*] Prestashop Version : %s %s' %(B,version,W))
    else:
        return print ('%s [!] Prestashop Version : %s %s' %(R,uknownversion,W))

# scan domain info
def domain_info():
    print ('%s [~] Search for SubDomains %s' %(Y,W))
    searchurl = "https://www.pagesinventory.com/search/?s=" + url
    getinfo = requests.get(searchurl,headers).text
    domains = []
    regex_domain = "<td><a href=\"\/domain\/(.*?).html\">"
    regex_ip = "<a href=\"/ip\/(.*?).html\">"
    regex_domain = re.compile(regex_domain)
    regex_ip = re.compile(regex_ip)
    matches_domain = regex_domain.findall(getinfo)
    match_ip = regex_ip.findall(getinfo)
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
    urldate = "https://input.payapi.io/v1/api/fraud/domain/age/" + uconvert(url)
    getinfo = requests.get(urldate,headers).text
    regex_date = r'Date: (.+?)-(.+?)'
    regex_date = re.compile(regex_date)
    matches = re.search(regex_date,getinfo)
    if matches:
        print ( '%s [*] Domain Created on : %s' % (B,matches.group(1)))
    ip = socket.gethostbyname(uconvert(url))
    print ( '%s [*] CloudFlare IP : %s' % (B,ip))
    ipinfo = "http://ipinfo.io/" + ip + "/json"
    getipinfo = requests.get(ipinfo,headers).text
    country = re.search(re.compile(r'country\": \"(.+?)\"'),getipinfo)
    region = re.search(re.compile(r'region\": \"(.+?)\"'),getipinfo)
    if country:
        print('%s [*] Country : %s' % (B,country.group(1)))
    if region:
        print('%s [*] Region : %s' % (B,region.group(1)))

#main
if __name__ == "__main__":
    args = parse_args()
    url = args.url
    file_name = args.file
    banner()
    detect_cms()