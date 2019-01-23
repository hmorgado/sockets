#!/usr/bin/python3.5

import socket
from shift import Shift

def main():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('localhost', 8085))
	serversocket.listen()
	
	conn, addr = serversocket.accept()
	with conn:
		print('connected by', addr)
		decrypt = Shift()
		while 1:
			data = conn.recv(1024)
			if not data or str.encode('exit') in data:
				break
			decrypted_msg = decrypt.shift('left', data.decode('utf-8'))
			print(decrypted_msg)


if __name__ == '__main__':
	main()