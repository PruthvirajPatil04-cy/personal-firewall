import platform
import subprocess

def block_ip(ip):
    system = platform.system()
    if system == "Linux":
        subprocess.call(f"sudo iptables -A INPUT -s {ip} -j DROP", shell=True)
    elif system == "Windows":
        subprocess.call(f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block remoteip={ip}', shell=True)
    else:
        print(f"Unsupported OS: {system}")
