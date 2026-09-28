import threading
import queue
from tkinter import *
from datetime import datetime
from packet_sniffer import start_sniffing

packet_queue = queue.Queue()

# Callback for every sniffed packet
def packet_callback(packet):
    timestamp = datetime.now().strftime("%H:%M:%S")
    summary = f"{timestamp} - {packet.summary()}"
    packet_queue.put(summary)

# GUI packet update loop
def update_gui():
    try:
        while not packet_queue.empty():
            packet = packet_queue.get_nowait()
            text_area.config(state='normal')
            text_area.insert(END, packet + "\n")
            text_area.see(END)
            text_area.config(state='disabled')
    except queue.Empty:
        pass
    root.after(100, update_gui)  # Refresh every 100ms

# Start background sniffing thread
def start_sniffing_thread():
    sniff_thread = threading.Thread(target=start_sniffing, args=(packet_callback,))
    sniff_thread.daemon = True
    sniff_thread.start()

# Set up GUI
root = Tk()
root.title("Personal Firewall - Live Packet Monitor")

text_area = Text(root, height=30, width=120, bg="black", fg="lime", font=("Consolas", 10), state='disabled')
text_area.pack(padx=10, pady=10)

start_sniffing_thread()
update_gui()

root.mainloop()
