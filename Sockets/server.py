import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)


while True:
	clientsocket, address = s.accept()
	print(f"Connecton form {address} has been establishted!")
	clientsocket.send(bytes("Welcome to the server!", "utf-8"))