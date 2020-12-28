import socket
import sys
from _thread import *

Host = ""
Port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

# Bind socket to local host mnd port
try:
    s.bind((Host, Port))
except socket.error:
    print("Bind Failed. Error Code :" + str(msg[0]) + "Message" + str(msg[1]))
    sys.exit()

print("Socket bind complete")

# Start listening on socket
s.listen(10)
print("Socket now listening")


# Function for handling connection. This will be used to create threads
def client_thread(conn):
    # Sending message to connected client
    conn.send(bytes("Welcome to the server. Type something and hit enter\n ", "utf-8"))  # send only takes strings

    # Infinite loop so that function do not terminate and thread do not end
    while True:
        # Receiving from client
        data = conn.recv(1024)
        reply = "OK..." + data.decode("utf-8")
        if not data:
            break
        conn.sendall(reply.encode("utf-8"))
    # came out of loop
    conn.close


# Now keep talking with the client
while 1:
    conn, addr = s.accept()
    print("Connected with " + addr[0] + ":", str(addr[1]))

    # Start new thread takes 1st argument as a function name to be run, second is the tuple of argument to the function
    start_new_thread(client_thread, (conn,))

s.close()
