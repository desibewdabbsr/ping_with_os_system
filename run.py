import os

# Read IP addresses from the file
with open('C:\\Users\\imper\\OneDrive\\Desktop\\IP_Address.txt') as file:
    ip_addresses = file.read().splitlines()

# Ping each IP address
for ip in ip_addresses:
    response = os.system(f"ping -c 1 {ip}")
    if response == 0:
        print(f"{ip} is up!")
    else:
        print(f"{ip} is down!")
