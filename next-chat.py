#!/usr/bin/python3.5

def encrypt(msg):
	secret_msg = ''
	for char in msg:
		secret_msg += chr(ord(char) + 1)
	return(secret_msg)


def decrypt(msg):
	secret_msg = ''
	for char in msg:
		secret_msg += chr(ord(char) - 1)
	return(secret_msg)


if __name__ == '__main__':
	print(encrypt('d'))
	print(decrypt('e'))