#!/usr/bin/env python3
import scapy.all as scapy # type: ignore

request = scapy.ARP()
#print(request.summary())
print(request.show())
print(scapy.ls(scapy.ARP()))

request.pdst = '192.168.1.53'

broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request 
# scapy.srp (send and receive packets)
answered_clients = scapy.srp(request_broadcast, timeout=1)[0]
for element in answered_clients:
    print(f'{element[1].psrc} : {element[1].hwsrc}')