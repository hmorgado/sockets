#!/usr/bin/python3.5

import socket

class mysocket:
	def __init__(self, sock=None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self, **kwargs):
		self.sock.connect((kwargs['host'], kwargs['port']))

	def send_it(self, msg):
		total_sent = 1
		msg_len = len(msg)
		while total_sent < msg_len:
			 							   # fun
			encoded_bytes_msg = str.encode(msg[0:total_sent])
			sent = self.sock.send(encoded_bytes_msg)
			print('sent byte num:', total_sent)
			if sent == 0:
				raise RunTimeError("socket conn broken")
			total_sent = total_sent + sent


def main():
	sender = mysocket()
	sender.connect(host='127.0.0.1', port=8080)
	sender.send_it('a b c d e f g h i j k l m n o p q r s \n')

if __name__ == '__main__':
	main()