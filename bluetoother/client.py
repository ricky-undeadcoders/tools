from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("20:2D:07:4B:A8:80", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
