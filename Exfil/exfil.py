from scapy.all import *
import base64


print("Program started.")
capture = rdpcap('Incident.pcap')
ping_data = ""

with open('out.png', 'ab') as file:

    for packet in capture:
        try:
            if packet[IP].src == '192.168.8.114':
                if packet.haslayer(ICMP):
                    x = bytes.fromhex(packet.load.hex()[32:64])
                    file.write(x)
        except IndexError:
            continue



print("Program finished.")
