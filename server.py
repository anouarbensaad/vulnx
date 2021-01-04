"""
Credits @lucmichalski

The simple example serving VULNX as a rest api.

instructions:

 pip install flasgger

 python server.py

open http://127.0.0.1:5000/apidocs/
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

from flasgger import Swagger

import logging
from logging.handlers import RotatingFileHandler

try:
    import simplejson as json
except ImportError:
    import json
try:
    from http import HTTPStatus
except ImportError:
    import httplib as HTTPStatus

from modules.detector import CMS
from modules.dorks.engine import Dork
from modules.dorks.helpers import DorkManual
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

valid_dorks_list = ['wordpress', 'prestashop', 'joomla', 'lokomedia', 'drupal', 'all']

HEADERS = {
    'User-Agent': random_UserAgent(),
    'Content-type' : '*/*',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

warnings.filterwarnings(
    action="ignore", message=".*was already imported", category=UserWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(
        epilog='\tExample: \r\npython ' + sys.argv[0] + " -p 5000 -h 0.0.0.0")
    parser.error = parser_error
    parser._optionals.title = "\nOPTIONS"
    parser.add_argument('--host',
                        help='server host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port',
                        help='server port', dest='port', type=int, default=5000)
    parser.add_argument('--log', type=str, default="/opt/vulnx/logs/access.log")
    return parser.parse_args()

def detection(url, opts):
    instance = CMS(
        url,
        headers=HEADERS,
        exploit=opts.exploit,
        domain=opts.subdomains,
        webinfo=opts.webinfo,
        serveros=True,
        cmsinfo=opts.cms,
        dnsdump=opts.dnsdump,
        port=opts.scanports
        )
    instance.instanciate()

def dork_engine(opts):
    if opts.dorks:
        DEngine = Dork(
            exploit=opts.dorks,
            headers=HEADERS,
            pages=(opts.numberpage or 1)
        )
        DEngine.search()

def dorks_manual(opts):
    if opts.dorkslist:
        DManual = DorkManual(
            select=opts.dorkslist
        )
        DManual.list()

def signal_handler(signal, frame):
    print("%s(ID: {}) Cleaning up...\n Exiting...".format(signal) % (W))
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

app = Flask(__name__)
CORS(app)

@app.route('/api',methods=['POST'])
def handle_vulnx():
    try:

        app.logger.info('request.json: %s', request.json)

        assert request.json["url"] , "Missing url"

        # search webs with dorks
        if "dork-list" in request.json:
            assert bool(request.json["dorks"]) == true, "Invalid dorks option"

        # specify search dorks number page limit
        if "number-pages" in request.json:
            assert int(request.json["number-pages"]) , "Invalid number-pages value"

        # specify input file of domains to scan
        if "dork-list" in request.json:
            assert bool(request.json["dork-list"] in valid_dorks_list) == true, "Invalid dork list option"

        # ports to scan
        if "ports" in request.json:
            assert isinstance(request.json["ports"], (list)), "Invalid ports option"

        ## Switches
        # searching vulnerability & run exploits
        if "exploit" in request.json:
            assert bool(request.json["exploit"]) == true, "Invalid exploit option"

        # search cms info[themes,plugins,user,version..]
        if "cms" in request.json:
            assert bool(request.json["cms"]) == true, "Invalid cms option"

        # web informations gathering
        if "web-info" in request.json:
            assert bool(request.json["web-info"]) == true, "Invalid web-info option"
        # request.json["web-info"]

        # subdomains informations gathering
        if "domain-info" in request.json:
            assert bool(request.json["domain-info"]) == true, "Invalid domain-info option"

        # dns informations gatherings
        if "dns" in request.json:
            assert bool(request.json["dns"]) == true, "Invalid dns option"

        opts = {}
        opts.url = request.json["url"]
        opts.dorks = request.json["dorks"]
        opts.numberpage = request.json["number-pages"]
        opts.dorkslist = request.json["dork-list"]
        opts.ports = request.json["ports"]
        opts.exploit = bool(request.json["exploit"])
        opts.cms = bool(request.json["cms"])
        opts.webinfo = bool(request.json["web-info"])
        opts.subdomains = bool(request.json["domain-info"])
        opts.dnsdump = bool(request.json["dns"])
        opts.output = "/app/reports/tempt.txt"

        app.logger.info('opts: %s', opts)
        # print("opts:")
        # print(opts)

        # vulnx
        dork_engine(opts)
        dorks_manual(opts)
        
        if opts.url:
            root = opts.url
            if root.startswith('http://'):
                opts.url = root
            elif root.startswith('https://'):
                opts.url=root.replace('https://','http://')
            else:
                opts.url = 'http://'+root
                print(opts.url)
            detection(opts)

        # if input_file:
        #     with open(input_file,'r') as urls:
        #         u_array = [url.strip('\n') for url in urls]
        #         try:
        #             for url in u_array:
        #                 root = url
        #             #url condition entrypoint
        #                 if root.startswith('http'):
        #                     url = root
        #                 else:
        #                     url = 'http://'+root
        #                 detection()
        #                 urls.close()
        #         except Exception as error:
        #             print('error : '+error)

        return jsonify(""), HTTPStatus.OK
    except IOError as e:
        return jsonify("Bad Request"), HTTPStatus.BAD_REQUEST
    except Exception as e:
        app.logger.info('request.json: %s', request.json)
        return jsonify(str(e)), HTTPStatus.BAD_REQUEST

if __name__ == "__main__":

    # cleaning screen
    banner()

    # args declaration
    args = parse_args()
    # url arg
    # url = args.url
    # input_file
    # input_file = args.input_file
    # Disable SSL related warnings
    warnings.filterwarnings('ignore')

    handler = RotatingFileHandler(args.log, maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host=args.host, port=args.port, debug=True)
