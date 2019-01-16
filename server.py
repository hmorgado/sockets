#!/usr/bin/python3.5

import socket

def main():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('127.0.0.1', 8081))
	server_socket.listen(5)

	while 1:
		(client_socket, address) = server_socket.accept()




if __name__ == '__main__':
	main()