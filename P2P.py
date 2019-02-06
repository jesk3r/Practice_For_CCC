import socket
import _thread 

def server():
	Servc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Servc.setsockopt(socket.SOL_SOCKET, socket .SO_REUSEADDR,1)
	Servc.bind((socket.gethostname(),3721))
	Servc.listen(5)
	return Servc

def client(servc):
	nsc, addr = servc.accept()
	print(nsc.recv(1024).decode("UTF-8"))
	nsc.send(str.encode("hello my guy"))
	# nsc.close	

while True:
	Servc = server()

	client(Servc)

	Servc.close()

