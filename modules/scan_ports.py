
#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)

from common.colors import que, portopen, portclose
from common.uriParser import parsing_url as hostd
import socket

portsobject = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    43: 'Whois',
    53: 'DNS',
    68: 'DHCP',
    80: 'HTTP',
    110: 'POP3',
    115: 'SFTP',
    119: 'NNTP',
    123: 'NTP',
    139: 'NetBIOS',
    143: 'IMAP',
    161: 'SNMP',
    220: 'IMAP3',
    389: 'LDAP',
    443: 'SSL',
    1521: 'Oracle SQL',
    2049: 'NFS',
    3306: 'mySQL',
    5800: 'VNC',
    8080: 'HTTP',
}

class ScanPort():
    def __init__(self,url,port):
        self.url = url
        self.port = port

    def portscan(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.port:
            result = sock.connect_ex((hostd(self.url), self.port))
            if result == 0:
                print(' {} {}                    {}   {}'
                    .format(que, self.port, portopen, portsobject[self.port]))
            else:
                print(' {} {}                    {}   {}'
                    .format(que, self.port, portclose, portsobject[self.port]))
