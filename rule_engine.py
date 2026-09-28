import json
from scapy.layers.inet import IP, TCP, UDP

def load_rules(filename="rules.json"):
    with open(filename, 'r') as f:
        return json.load(f)

def match_rule(packet, rules):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        for rule in rules:
            if rule.get("ip") in [src_ip, dst_ip] and rule["action"] == "block":
                return True, f"Blocked IP: {rule['ip']}"

            if rule.get("port"):
                if TCP in packet or UDP in packet:
                    sport = packet.sport
                    dport = packet.dport
                    if rule["port"] in [sport, dport] and rule["action"] == "block":
                        return True, f"Blocked Port: {rule['port']}"

            if rule.get("protocol"):
                if rule["protocol"].upper() in packet.summary() and rule["action"] == "block":
                    return True, f"Blocked Protocol: {rule['protocol']}"

    return False, ""
