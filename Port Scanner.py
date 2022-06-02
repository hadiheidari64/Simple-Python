import pyfiglet
import sys
import socket
from datetime import datetime


ascii_banner = pyfiglet.figlet_format("PORT SCANNER BY El3ct0r")
print(ascii_banner)

#Ask the user to inout the hostname to scan
target = input("input your hostname: ")

if len(sys.argv) == 2:

    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

# Add Banner
print("-" * 50)
print(f"Scanning Target:\n {target}")
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:

    # will scan ports between 1 to 65,535(for now I put 1023)
    for port in range(1, 1023):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname was not Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ not response from server !!!!")
    sys.exit()
