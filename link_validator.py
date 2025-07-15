import os
from icmplib import ping
from icmplib.exceptions import NameLookupError

def host_up(hostname: str):
    try:
        host = ping(hostname, count=5, interval=0.2, timeout=1, privileged=False)
    except NameLookupError:
        return False
    print(f"Sent: {host.packets_sent}, Received: {host.packets_received}")
    return host.packets_sent == host.packets_received

directory = os.fsencode('/output/links/')

for file in os.listdir(directory):
    with open(file) as f:
        list_of_links = f.readlines()
        for link in list_of_links:
            link = link.strip().replace(" ", "")
            print(link)
            if host_up(link):
                print(f"{link} is valid")
            else:
                print(f"{link} is not valid")