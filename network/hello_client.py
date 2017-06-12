import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print(str(s.recv(1024)))

print(s.send(bytes("hello server", "utf8")))
s.close()                     # Close the socket when done
