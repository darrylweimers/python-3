import socket


ADDRESS = '127.0.0.1'
PORT = 9999


class ClientSocket(object):

    def __init__(self, host=ADDRESS, port=PORT):
        super().__init__()
        self._host = host
        self._port = port

    def send(self, data: bytes):
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self._host, int(self._port)))
            sock.sendall(data)
            raw_rx = sock.recv(1024)
        return raw_rx


client_socket = ClientSocket()
data_rx = client_socket.send(bytes('data'.encode('utf-8')))



# socket
# is an endpoint for communication between two machines
# where medium can be LAN, WAN or internet
# socket can use TCP/UDP protocols

# server
# a machine that waits for client requests to serve or process them
# hosts a port and ip address (default 127.0.0.1)
# port: should be anything above 1024 as value from 0 - 1024 are occupied by core services


# client
# a requester of services



    # Connect to server and send data