#!/usr/bin/env python
#Auther : BENSAAD Anouar
import socket
import time
import sys
import signal

data = 1024
server_sock = None
def mrecv(c):
    tab = []
    bytes_recd = 0
    while bytes_recd < data:
        data = c.recv(min(data - bytes_recd, 2048))
        if not data: break
        tab.append(data)
        bytes_recd = bytes_recd + len(data)
    return ''.join(tab)

def prequest(c,addr,datainput):
	try:
		data = datainput.decode('utf-8')
		list = data.split(' ')
		method = list[0]
		requested_file = list[1]
		print	('Method: ', method)
		print  ' Hacker: ', addr
		print  'This Hacker ',addr
		print	'Scanning Nmap for ', data
		file = requested_file.split('?')[0]
		file = file.lstrip('/')
	except Exception, e:
		print e

		
def signal_exit(sig, frame):
	global server_sock
	server_sock.shutdown(SHUT_WR)
	print('You pressed Ctrl+C!')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_exit)

def Main():
	
	server_sock = socket.socket()
	server_name = ''
	server_port = 1234
	server_sock.bind((server_name, server_port))
	print 'Starting Server ON', server_name, server_port

	server_sock.listen(5)
	try:
		while 1:
			data = None
			(c,addr) = server_sock.accept()
			try:
				data = mrecv(c)
			except socket.error, ex:
				print ex
			if data : prequest(c,addr,data)
			c.close()
	except Exception, ex:
		print ex
		server_sock.close()
 

if __name__== '__main__' :

        Main ()

