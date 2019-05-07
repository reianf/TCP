import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)
try: 
	#Send user input data
	message = input("Enter message: ")
	while len(message) > 256:
		print("Error: Input exceeds 256 characters. Try again.")
		message = input("Enter message: ")	
	print("Sending: ", message)
	sock.sendall(message.encode())

	#Look for the response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(256)
		amount_received += len(data)
		print("Received: ", data.decode())

finally:
	print('Closing socket')
	sock.close()
