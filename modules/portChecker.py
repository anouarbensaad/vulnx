
from common.colors import que, portopen, portclose
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


def portscan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if port:
        result = sock.connect_ex((host, port))
        if result == 0:
            print(' %s %s                    %s   %s' %
                  (que, port, portopen, portsobject[port]))
        else:
            print(' %s %s                    %s   %s' %
                  (que, port, portclose, portsobject[port]))
