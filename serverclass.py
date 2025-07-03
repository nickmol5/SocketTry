import socket

class Server: 
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = None
		self.clients = {}

	def create(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))
	
	def listen(self, num_clientes):
		self.sock.listen(num_clientes)

	def accept_connection(self, name):
		client, addr = self.sock.accept()
		self.clients[name] = {
			'socket': client,
			'address': addr
		}
	
	def 
	

	