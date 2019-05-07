import socket
import sys

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the socket to the port
server_address = ('localhost', 10000)
print("starting up on %s port %s" % server_address)
sock.bind(server_address)
#Listen for incoming connections
sock.listen(1)

while True:
	print("Waiting for a connection")
	connection, client_address = sock.accept()
	try:
		print("Connection from", client_address)

		#Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(256)
			print("Received: ", data.decode())
			
			#convert message
			result = ''
			
			for char in data.decode():
				x = ord(char) + 1
				while x < 32:
					x += 96
				while x > 127:
					x -= 96
				result += chr(x)

			data = result.encode()
			
			if data:
				print("Sending data back to the client")
				connection.sendall(data)
			else:
				print("No more data from ", client_address)
				break

	finally:
		connection.close()
