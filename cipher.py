class Cipher():
	def dispatch_dict(operator, msg):
		return {
			'left_shift': "".join([ chr(ord(x) - 3) for x in msg ]),
			'right_shift': "".join([ chr(ord(x) + 3) for x in msg ])
		}.get(operator, '')

if __name__ == '__main__':

	print(dispatch_dict('left_shift', 'heitor'))
	print(dispatch_dict('right_shift', 'ebfqlo'))