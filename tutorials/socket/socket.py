import socket

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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data