#!/usr/bin/python3.5

import socket
from shift import Shift

class mysocket:
	def __init__(self, sock=None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self, **kwargs):
		self.sock.connect((kwargs['host'], kwargs['port']))

	def send_it(self, msg):
		total_sent = 0
		msg_len = len(msg)
		while total_sent < msg_len:
			encoded_bytes_msg = str.encode(msg[total_sent:])
			sent = self.sock.send(encoded_bytes_msg)
			if sent == 0:
				raise RunTimeError("socket conn broken")
			total_sent = total_sent + sent

# tcpdump -nnXSs 1514 port 8085 -i lo

def main():
	sender = mysocket()
	sender.connect(host='127.0.0.1', port=8085)
	encrypt = Shift()
	while 1:
		msg = input('enter msg: ')
		if 'exit' in msg:
			break

		encrypted_msg = encrypt.shift('right', msg)
		sender.send_it(encrypted_msg)

if __name__ == '__main__':
	main()