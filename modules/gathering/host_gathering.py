import requests
import re
import socket
from common.colors import bad,que, info, good,run,W,end
from common.uriParser import parsing_url as hostd

class GatherHost():

    def __init__(self,url,headers=None):
        self.url = url
        self.headers = headers

    def match_info(self,regex,data):
        match = re.search(regex, data)
        if match:
            return dict(
                data=match.group(1)
            )
    def match_printer(self,to_match,match):
        if match['data']:
            print(' {} {} : {}'.format(good,to_match,match))

    def os_server(self):
        response = requests.get(self.url, headers=self.headers).headers
        try:
            if response["server"]:
                regx = re.compile(r"(.+) \((.+)\)")
                data = regx.search(response["server"])
                print(' {} {}Server :{} {}' .format(good, W, end, data.group(1)))
                print(' {} {}OS :{} {}' .format(good, W, end, data.group(2)))
        except KeyError:
            print(' {} Cannot Match the server headers ' .format(bad))

    def web_host(self):
        urldate = "https://input.payapi.io/v1/api/fraud/domain/age/" + hostd(self.url)
        getinfo = requests.get(urldate, self.headers).text
        regex_date = r'Date: (.+?)-(.+?)'
        regex_date = re.compile(regex_date)
        matches = re.search(regex_date, getinfo)
        
        print(' {} Web Hosting Information'.format(run))
        
        if matches:
            print(' {} Domain Created on : {}'.format(good, matches.group(1)))
        try:
            ip = socket.gethostbyname(hostd(self.url))
            print(' {} CloudFlare IP : {}'.format(good, ip))
            ipinfo = "http://ipinfo.io/" + ip + "/json"
            gather = requests.get(ipinfo, self.headers).text

            self.match_printer('Country',self.match_info(r'country\": \"(.+?)\"',gather))
            self.match_printer('Region',self.match_info(r'region\": \"(.+?)\"',gather))
            self.match_printer('Latitude',self.match_info(r'latitude: (.+?)',gather))
            self.match_printer('Longitude',self.match_info(r'longitude\": \"(.+?)\"',gather))
            self.match_printer('Timezone',self.match_info(r'timezone\": \"(.+?)\"',gather))
            self.match_printer('Ans',self.match_info(r'ans\": \"(.+?)\"',gather))
            self.match_printer('Org',self.match_info(r'org\": \"(.+?)\"',gather))

        except Exception as parsing_error:
            print(' %s Parsing error : %s' % (bad, str(parsing_error)))