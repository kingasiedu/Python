import socket  # for sockets
import sys  # for exit

try:
    # create an AF_INET, STREAM socket(TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket. Error code:" + str(msg[0]) + "Error code" + str(msg[1]))
    sys.exit()

print("Socket Created")

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    # could not resolve
    print("Host name could not resolve. Exiting")
    sys.exit()

print("Ip Address of " + host + " is " + remote_ip)

# connect to remote server
s.connect((remote_ip, port))

print("Socket Connected to " + host + " on ip " + remote_ip)

# send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Set the whole string
    s.sendall(bytes(message, "utf-8"))
except socket.error:
    print("Send failed")
    sys.exit()
print("Message send successfully")


# Receive data from server
reply = s.recv(4096)
print(reply)

s.close()
