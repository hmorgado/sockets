class Shift():
	def shift(self, direction, msg):
		return {
			'left': "".join([chr(ord(x) - 3) for x in msg]),
			'right': "".join([chr(ord(x) + 3) for x in msg])
		}.get(direction, '')

if __name__ == '__main__':
	print(dispatch_dict('left', 'heitor'))
	print(dispatch_dict('right', 'ebfqlo'))