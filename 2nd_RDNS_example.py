import socket
import sys
import ipaddress
ip = []
for times in range(5):
    try:
        ip_address = (input("Enter an Ip Address:"))
    except:
        ip_address = input("Enter an Ip Address:")
    ip.append(ip_address)
    # if ip_address < 5:
    # print(input("Please enter an IP Address"))
    # else:
    # continue

for ip_address in ip:
    rev_dns = socket.gethostbyaddr(ip_address)
    # DNS Host name
    print("% -16s %s" % ("DNS Hostname", rev_dns[0]))
    # DNS Alias
    print("% -16s % s" % ("DNS Alias(s)", rev_dns[1]))
    # ip address
    print("% -16s % s" % ("IP address(s)", rev_dns[2]))

