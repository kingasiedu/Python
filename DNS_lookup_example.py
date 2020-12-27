import sys, socket 
try:
    ses = socket.gethostbyaddr("18.216.114.70")
    print("The host name is:")
    print("" + ses[0])
    print("\n Address:")
    for i in ses[2]:
        print("" + i)
except socket.herror:
    print("Error resolving ip address")
