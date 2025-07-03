import socket

'''
USE: Ejecuta primero el codigo del servidor, y en otra terminal ejecuta el codigo del cliente
'''

class Server: 
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = None
		self.client_socket = None

	def create(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))
	
	def listen(self, num_clientes):
		self.sock.listen(num_clientes)

	def accept_connection(self):
		self.client_socket, addr = self.sock.accept()
		print(f'Server connected to {addr}')
		print("If you wanna leave, press '0'\n")
	
	def receive_message(self):
		message = self.client_socket.recv(1024).decode()
		if message == '0':
			self.client_socket.close()
			return False
		print(f'Client: {message}')
		return True

	
	def send_message(self):
		message = input('Server: ')
		self.client_socket.send(message.encode())
		if message == '0':
			self.client_socket.close()
			return False
		return True
		
def main(): 
	server = Server('localhost', 9999)
	server.create()
	server.listen(1)
	server.accept_connection()
	while True:
		if not server.receive_message():
			print('\nNo message received from the client')
			break
		if not server.send_message():
			print('\nConnection closed')
			break

main()