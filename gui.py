import tkinter as tk
from tkinter import scrolledtext

class FirewallGUI:
    def __init__(self, master):
        self.master = master
        master.title("Personal Firewall")
        master.geometry("800x500")

        self.log_area = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.log_area.pack(fill=tk.BOTH, expand=True)

        self.status_label = tk.Label(master, text="Status: Running", fg="green")
        self.status_label.pack()

    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
