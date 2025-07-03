import socket

class Client:
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.socket = None
		self.state = True

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.host, self.port))

	def send_message(self): 
		message = input('You: ')
		if message == 0:
			self.socket.close()
			return
		self.socket.send(message.encode())

	def receive_message(self):
		data = 