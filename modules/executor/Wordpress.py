
#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)

from modules.exploits.wordpress_exploits import WPExploits
from modules.gathering.host_gathering import GatherHost
from modules.gathering.wpcms import wp_plugin,wp_themes,wp_user,wp_version
from modules.dns_dump import dnsdumper,domain_info
from modules.scan_ports import ScanPort
import sys


class Wordpress(object):
    """
    call it when target is a wordpress cms.
    Usings method from other class.
    """

    def __init__(self, url=None, headers=None, port=None):
        
        # init the url & headers.
        self.url = url
        self.headers = headers
        # port to scan
        self.port = port

    def exploit(self):
        wpx = WPExploits(self.url, self.headers)
        return wpx.wpexploits()

    def webinfo(self):
        whg = GatherHost(self.url,self.headers)
        whg.web_host()

    def serveros(self):
        whg = GatherHost(self.url,self.headers)
        whg.os_server()

    def cmsinfo(self):
        wp_plugin(self.url,self.headers)
        wp_themes(self.url,self.headers)
        wp_user(self.url,self.headers)
        wp_version(self.url,self.headers)

    def dnsdump(self):
        return dnsdumper(self.url)

    def domaininfo(self):
        return domain_info(self.url)

    def ports(self,port):
        self.port = port
        sp = ScanPort(self.url,self.port)
        sp.portscan()
