from argparse import ArgumentParser
from scapy.all import ARP, Ether, srp

#Parser for inputting target IP address

parser=ArgumentParser(
    prog="Network Scanner",
    description= "This is a basic network scanner using ARP."
)

parser.add_argument('-t', help="Specify the target IP address using the syntax -t  in CIDR notation.", required=True)
args=parser.parse_args()

target_ip = args.t #"192.168.178.1/24"
# ARP request to inquire about the MAC address belonging to the specified IP address
arp=ARP(pdst=target_ip)

# Ethernet broadcast packet to the broadcast MAC address
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

#Stack ether and arp to create packet
packet = ether/arp

#Send and receive layer 2 packets, result is list of pairs of (sent_packet, received packet)
result = srp(packet, timeout=3, verbose=0)[0]
clients=[]
for sent, received in result:
    #Fill out result list with acquired IP and MAC addresses
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

#Print results
print("Available devices on this network:")
print("IP"+" "*20+"MAC")
for client in clients:
    print("{:16}     {}".format(client['ip'], client['mac']))
