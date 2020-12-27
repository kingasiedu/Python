import socket
import sys

HOST = ""
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")
# bind the socket to the port
try:
    s.bind((HOST, PORT))
except socket.error:
    print("Bind Failed. Error Code:" + str(msg[0]) + "Message" + str(msg[1]))
    sys.exit()
print("Socket bind complete")

# Listen for connection
s.listen(10)
print("Socket now listening")

# Wait to accept a connection  - blocking call
conn, addr = s.accept()

# Display client information
print("Connected with " + addr[0] + ":", str(addr[1]))

#now keep talking with the client 
data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()

