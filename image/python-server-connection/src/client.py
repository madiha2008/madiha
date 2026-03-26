class Client:
    def __init__(self, server_address, port):
        self.server_address = server_address
        self.port = port
        self.connection = None

    def connect(self):
        import socket
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.server_address, self.port))

    def send_data(self, data):
        if self.connection:
            self.connection.sendall(data.encode('utf-8'))

    def receive_data(self):
        if self.connection:
            return self.connection.recv(1024).decode('utf-8')

    def close_connection(self):
        if self.connection:
            self.connection.close()