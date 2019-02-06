import socket

def clinet():
	f = open("/Users/dheeraj/Documents/testrandcode/test_dns_node", 'r')

	line = f.readline()

	s = socket.socket()


	while line:
		try:
			s.connect(('{0}'.format(line), 5555)

		except: 
			print('{0} did not except our connction'.format(line))
			line = f.readline()

			