from datetime import datetime

def log_suspicious(packet, reason, log_file="logs/suspicious.log"):
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now()}] {reason} - {packet.summary()}\n")
