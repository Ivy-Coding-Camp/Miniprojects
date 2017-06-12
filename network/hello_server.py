import socket               # Import socket module
from threading import Thread

class DedicatedServerThread(Thread):
    def __init__(self, connection, ip_address):
        Thread.__init__(self)
        self.connection = connection
        self.ip_address = ip_address
        print("Dedicated Server Thread started for client "+str(ip_address))

    def run(self):
        while True:
            self.connection.send(bytes("Thanks for connecting..","utf8"))
            data = self.connection.recv(2048)
            if not data: break
            print("received data:"+str(data))
            self.connection.send(data)  # echo

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()                                     # Get local machine name
port = 12345                                                    # Reserve a port for your service.
s.bind((host, port))                                            # Bind to the port
ds_threads = list()

while True:
    s.listen(5)  # Now wait for client connection.
    conn, addr = s.accept()     # Establish connection with client.
    ds_thread = DedicatedServerThread(conn, addr)
    ds_thread.start()
    ds_threads.append(ds_thread)

for t in ds_threads:
    t.join()
