

#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)

import requests
import re
import base64
import json
from common.colors import red, green, bg, G, R, W, Y, G, good, bad, run, info, end, que, bannerblue
from bs4 import BeautifulSoup
from common.uriParser import parsing_url as hostd


def results(table):
    res = []
    trs = table.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        pattern_ip = r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
        try:
            ip = re.findall(pattern_ip, tds[1].text)[0]
            domain = str(tds[0]).split('<br/>')[0].split('>')[1]
            header = ' '.join(tds[0].text.replace('\n', '').split(' ')[1:])
            reverse_dns = tds[1].find('span', attrs={}).text

            additional_info = tds[2].text
            country = tds[2].find('span', attrs={}).text
            autonomous_system = additional_info.split(' ')[0]
            provider = ' '.join(additional_info.split(' ')[1:])
            provider = provider.replace(country, '')
            data = {'domain': domain,
                    'ip': ip,
                    'reverse_dns': reverse_dns,
                    'as': autonomous_system,
                    'provider': provider,
                    'country': country,
                    'header': header}
            res.append(data)
        except:
            pass
    return res


def text_record(table):
    res = []
    for td in table.findAll('td'):
        res.append(td.text)
    return res


def dnsdumper(url):

    '''
    For DNS Dump you retrieve token from dnsdumpster.
    V   T    X
    |  / |  /
    | /  | /
    U -> N
    |  /    Parsing data from records
    | /     MX , Domains , DNS , MAILS 
    L
    Schema V, returns set of (U, L, N, T, X)
    '''
    
    domain = hostd(url)
    dnsdumpster_url = 'https://dnsdumpster.com/'
    response = requests.Session().get(dnsdumpster_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # If no match is found, the return object won't have group method, so check.
    try:
        csrf_token = soup.findAll(
            'input', attrs={'name': 'csrfmiddlewaretoken'})[0]['value']
    except AttributeError:  # No match is found
        csrf_token = soup.findAll(
            'input', attrs={'name': 'csrfmiddlewaretoken'})[0]['value']
    print(' %s Retrieved token: %s' % (info, csrf_token))
    cookies = {'csrftoken': csrf_token}
    headers = {'Referer': 'https://dnsdumpster.com/'}
    data = {'csrfmiddlewaretoken': csrf_token, 'targetip': domain}
    response = requests.Session().post('https://dnsdumpster.com/',
                                       cookies=cookies, data=data, headers=headers)
    image = requests.get('https://dnsdumpster.com/static/map/%s.png' % domain)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.findAll('table')
        res = {}
        res['domain'] = domain
        res['dns_records'] = {}
        res['dns_records']['dns'] = results(tables[0])
        res['dns_records']['mx'] = results(tables[1])
        print(' %s Search for DNS Servers' % que)
        for entry in res['dns_records']['dns']:
            print((" %s Host : {domain} \n %s IP : {ip} \n %s AS : {as} \n  %s----------------%s".format(
                **entry) % (good, good, good, bannerblue, end)))
        print(' %s Search for MX Records ' % que)
        for entry in res['dns_records']['mx']:
            print((" %s Host : {domain} \n %s IP : {ip} \n %s AS : {as} \n  %s----------------%s".format(
                **entry) % (good, good, good, bannerblue, end)))


def domain_info(url):
    domain = hostd(url)
    dnsdumpster_url = 'https://dnsdumpster.com/'
    response = requests.Session().get(dnsdumpster_url).text
    # If no match is found, the return object won't have group method, so check.
    try:
        csrf_token = re.search(
            r"name='csrfmiddlewaretoken' value='(.*?)'", response).group(1)
    except AttributeError:  # No match is found
        csrf_token = re.search(
            r"name='csrfmiddlewaretoken' value='(.*?)'", response)
    cookies = {'csrftoken': csrf_token}
    headers = {'Referer': 'https://dnsdumpster.com/'}
    data = {'csrfmiddlewaretoken': csrf_token, 'targetip': domain}
    response = requests.Session().post('https://dnsdumpster.com/',
                                       cookies=cookies, data=data, headers=headers)
    image = requests.get('https://dnsdumpster.com/static/map/%s.png' % domain)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.findAll('table')
        res = {}
        res['domain'] = domain
        res['dns_records'] = {}
        res['dns_records']['host'] = results(tables[3])
        print(' %s SubDomains' % que)
        for entry in res['dns_records']['host']:
            print((" %s SubDomain : {domain} \n %s IP : {ip} \n %s----------------%s".format(
                **entry) % (good, good, bannerblue, end)))
