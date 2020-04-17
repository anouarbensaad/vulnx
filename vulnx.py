
#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)

"""
The vulnx main part.
Author: anouarbensaad
Desc  : CMS-Detector and Vulnerability Scanner & exploiter
Copyright (c)
See the file 'LICENSE' for copying permission
"""

from modules.detector import CMS
from common.colors import red, green, bg, G, R, W, Y, G, good, bad, run, info, end, que, bannerblue2

from common.requestUp import random_UserAgent
from common.uriParser import parsing_url as hostd
from common.banner import banner

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


warnings.filterwarnings(
    action="ignore", message=".*was already imported", category=UserWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

# cleaning screen

banner()

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()


def parse_args():
    parser = argparse.ArgumentParser(
        epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
    parser.error = parser_error
    parser._optionals.title = "\nOPTIONS"
    parser.add_argument('-u', '--url', help="url target to scan")
    parser.add_argument(
        '-D', '--dorks', help='search webs with dorks', dest='dorks', type=str)
    parser.add_argument(
        '-o', '--output', help='specify output directory', required=False)
    parser.add_argument(
        '-t', '--timeout', help='http requests timeout', dest='timeout', type=float)
    parser.add_argument('--threads', help="number of threads",
                        dest='numthread', type=float)
    parser.add_argument('-n', '--number-pages',
                        help='search dorks number page limit', dest='numberpage', type=int)
    parser.add_argument(
        '-i', '--input', help='specify input file of domains to scan', dest='input_file', required=False)
    parser.add_argument('-l', '--dork-list', help='list names of dorks exploits', dest='dorkslist',
                        choices=['wordpress', 'prestashop', 'joomla', 'lokomedia', 'drupal', 'all'])
    parser.add_argument('-p',  '--ports', help='ports to scan',
                        dest='scanports', type=int)
    # Switches
    parser.add_argument('-e', '--exploit', help='searching vulnerability & run exploits',
                        dest='exploit', action='store_true')
    parser.add_argument('--it', help='interactive mode.',
                        dest='cli', action='store_true')

    parser.add_argument('--cms', help='search cms info[themes,plugins,user,version..]',
                        dest='cms', action='store_true')

    parser.add_argument('-w', '--web-info', help='web informations gathering',
                        dest='webinfo', action='store_true')
    parser.add_argument('-d', '--domain-info', help='subdomains informations gathering',
                        dest='subdomains', action='store_true')
    parser.add_argument('--dns', help='dns informations gatherings',
                        dest='dnsdump', action='store_true')

    return parser.parse_args()

# args declaration
args = parse_args()
# url arg
url = args.url
# interactive arugment
cli = args.cli
# run exploit
exploit = args.exploit
# cms gathering args
cms = args.cms
# dorks search.
dorks = args.dorks
dorkslist = args.dorkslist
# timeout
timeout = args.timeout or 3
# thread
numthread = args.numthread or 1
# numberpage
numberpage = args.numberpage or 1
# input_file
input_file = args.input_file
# Disable SSL related warnings
warnings.filterwarnings('ignore')

def detect_cms():

    instance = CMS(
        url,
        headers=headers,
        exploit=args.exploit,
        domain=args.subdomains,
        webinfo=args.webinfo,
        serveros=True,
        cmsinfo=args.cms,
        dnsdump=args.dnsdump,
        port=args.scanports
            )
    instance.instanciate()

# output
output_dir = args.output or 'logs'

if not os.path.exists(output_dir):  # if the directory doesn't exist
    os.mkdir(output_dir)  # create a new directory

def signal_handler(signal, frame):
    print("%s(ID: {}) Cleaning up...\n Exiting...".format(signal) % (W))
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":

    if input_file:
        with open(input_file, 'r') as urls:
            u_array = [url.strip('\n') for url in urls]
            try:
                for url in u_array:
                    root = url
                # url condition entrypoint
                    if root.startswith('http'):
                        url = root
                    else:
                        url = 'http://'+root
                    # default headers.
                    headers = {
                        'User-Agent': random_UserAgent(),
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Connection': 'keep-alive',
                    }
                    detect_cms()
                    urls.close()
            except Exception as error_:
                print('UKNOWN ERROR : ' + str(error_))

    if url:
        # url condition entrypoint
        root = url
        if root.startswith('http'):
            url = root
            print(url)
        elif root.startswith('https'):
            url=root.replace('https','http')
            
            print(url)
        else:
            url = 'http://'+root
            print(url)
        # default headers.
        headers = {
            'User-Agent': random_UserAgent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        detect_cms()