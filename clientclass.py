import socket

'''
USE: Ejecuta primero el codigo del servidor, y en otra terminal ejecuta el codigo del cliente
'''

class Client:
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.socket = None

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.host, self.port))
		print("Connected to the server, if you want to leave press '0'\n")

	def send_message(self): 
		message = input('You: ')
		self.socket.send(message.encode())
		if message == '0':
			self.socket.close()
			return False
		return True

	def receive_message(self):
		data = self.socket.recv(1024).decode()
		if data == '0':
			self.socket.close()
			return False
		print(f'Server: {data}')
		return True


def main():
	client = Client('localhost', 9999)
	client.connect()
	while True:
		if not client.send_message():
			print('\nConnection closed')
			break
			
		if not client.receive_message():
			print('\nNo message received from the server ')
			break

main()
