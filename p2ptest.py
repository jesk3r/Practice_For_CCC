import socket

def client():
	try:
		s = socket.socket()
		s.connect(("99.234.34.129",3721))
		return s
	except:
		print("something went wrong")	


def recvmsg(Sc):
	 data = sc.recv(1028)
	 print(data.decode("UTF-8"))

	
def sendmsg(inf, msg):	
	inf.send(str.encode(msg))


sc = client()

while True:	
	
	sendmsg(sc, input("what msg would you like to send"))

	recvmsg(sc)

