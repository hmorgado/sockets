#!/usr/bin/python3.5

import socket

def main():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('localhost', 8086))
	serversocket.listen()
	
	conn, addr = serversocket.accept()
	with conn:
		print('connected by', addr)
		while 1:
			data = conn.recv(1024)
			if not data:
				break
			print(str.encode('exit') in data)
			conn.sendall(data)


if __name__ == '__main__':
	main()