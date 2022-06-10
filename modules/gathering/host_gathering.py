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
            print(' {0} {1} : {2}'.format(good,to_match,match['data']))

    def os_server(self):

        response = requests.get(self.url, headers=self.headers,verify=False).headers
        try:
                regx = re.compile(r"(.+) \((.+)\)")
                data = regx.search(response["server"])
                try:
                    print(' {0} {1}Server :{2} {3}' .format(good, W, end, data.group(1)))
                    print(' {0} {1}OS :{2} {3}' .format(good, W, end, data.group(2)))
                except AttributeError:
                    print(' {0} Cannot Find OS & HostingServer ' .format(bad))
        except KeyError:
            print(' {0} Cannot Find the server headers ' .format(bad))

    def web_host(self):
        urldate = "https://input.payapi.io/v1/api/fraud/domain/age/" + hostd(self.url)
        getinfo = requests.get(urldate, self.headers,verify=False).text
        regex_date = r'Date: (.+?)-(.+?)'
        regex_date = re.compile(regex_date)
        matches = re.search(regex_date, getinfo)
        try:
            if matches:
                print(' {0} Domain Created on : {1}'.format(good, matches.group(1)))
                ip = socket.gethostbyname(hostd(self.url))
                print(' {0} CloudFlare IP : {1}'.format(good, ip))
                ipinfo = "http://ipinfo.io/" + ip + "/json"
                gather = requests.get(ipinfo, self.headers).text

                self.match_printer('Country',self.match_info(r'country\": \"(.+?)\"',gather))
                self.match_printer('Region',self.match_info(r'region\": \"(.+?)\"',gather))
                self.match_printer('Timezone',self.match_info(r'timezone\": \"(.+?)\"',gather))
                self.match_printer('Postal',self.match_info(r'postal\": \"(.+?)\"',gather))
                self.match_printer('Org',self.match_info(r'org\": \"(.+?)\"',gather))
                self.match_printer('Location',self.match_info(r'loc\": \"(.+?)\"',gather))
        except Exception as err:
            print(' {0} Parse Error : {1}' .format(bad,err))