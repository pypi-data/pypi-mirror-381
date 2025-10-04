import ipaddress
import socket

def searchIP(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'The {host} IP Address is {socket.gethostbyname(host)}')
def connectIP(ip, MessageStart):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 8080))
    print(MessageStart)
def get_info_ip(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # initialize an IPv4 Address
    ip = ipaddress.IPv4Address(ip)

    # print True if the IP address is global
    print("Is global:", ip.is_global)

    # print Ture if the IP address is Link-local
    print("Is link-local:", ip.is_link_local)

    # initialize an IPv4 Network
    network = ipaddress.IPv4Network(ip)

    # get the network mask
    print("Network mask:", network.netmask)

    # get the broadcast address
    print("Broadcast addressdr:", network.broadcast_address)

    # print the number of IP adesses under this network
    print("Number of hosts under", str(network), ":", network.num_addresses)

    # get the supernet of this network
    print("Supernet:", network.supernet(prefixlen_diff=1))

    # iterate over the subnets of this network
    print("Subnets:")
    for subnet in network.subnets(prefixlen_diff=2):
        print(subnet)
