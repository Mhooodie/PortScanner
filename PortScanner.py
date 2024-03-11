import socket
import sys
from datetime import datetime

print("--------------------")
print("PORT SCANNER")
print("--------------------")

# target = input("Please Enter host to Scan: ")
target = input("Please Enter host to Scan: ")
host = socket.gethostbyname(target)

print(f"Target: {target}")
print(f"Host: {host}")

try:
    file = open("Port-Scanner-Info.txt", "w") # r Read w Write etc...
except FileExistsError:
    print("File Exists Error. Exiting")
    sys.exit()

date = datetime.date(datetime.now())
t1 = datetime.now()

print("Start Time: {}".format(t1.strftime("%H:%M:%S\n"))) # .strf seperates time so you can choose Hr Min Sec etc...
file.write("Start Time: {} \n\n".format(t1.strftime("%H:%M:%S")))

try:

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET for IPv4 (add a 6 for IPv6) & SOCK_STREAM for TCP & SOCK_DGRAM for UDP
        sock.settimeout(0.001)
        result = sock.connect_ex((host, port))

        if result == 0:
            try:
                print("Port No : {} Open Protocal Service Name: {}".format(port, socket.getservbyport(port, "tcp")))
                file.write("\nPort No : {} Open Protocal Service Name: {}".format(port, socket.getservbyport(port, "tcp")))
            except socket.error:
                print("Port No : {} Open Protocal Service Name: {}".format(port, "Unknown"))
                file.write("\nPort No : {} Open Protocal Service Name: {}".format(port, "Unknown"))
        # else:
        #     print("Port No : {} Closed".format(port)) #FINDS CLOSED PORTS
                
except socket.gaierror:
    print("HostName could not be resolved. Exiting")
    file.write("\n\nHostName could not be resolved. Exiting")
    sys.exit()
except socket.error:
    print("Couldn't Connect to Server. Exiting")
    file.write("\n\nCouldn't Connect to Server. Exiting")
    sys.exit()

t2 = datetime.now()
print("\nEnd Time: {}".format(t2.strftime("%H:%M:%S")))
file.write("\n\nEnd Time: {}".format(t2.strftime("%H:%M:%S")))

total_time = t2 - t1
print("Total Time: {}".format(total_time, "\n"))
file.write("\n\nTotal Time: {}".format(total_time))