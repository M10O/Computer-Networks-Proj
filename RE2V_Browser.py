import socket
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.connect(("google.com", 80))
cmd = 'GET http://www.google.com/\r\n\r\n\'.encode()
new_socket.send(cmd)

while True:
	data = new_socket.recv(512)
	if len(data)<1:
		break
	print(data.decode(), end='')

new_socket.close()