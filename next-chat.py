#!/usr/bin/python3.5

def main():
	secret_msg = ''
	for char in 'abc':
		secret_msg += chr(ord(char) + 1)

	print(secret_msg)

if __name__ == '__main__':
	main()