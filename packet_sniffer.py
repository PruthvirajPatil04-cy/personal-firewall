from scapy.all import sniff

def start_sniffing(packet_callback):
    sniff(prn=packet_callback, store=False)