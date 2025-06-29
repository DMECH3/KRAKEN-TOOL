from scapy.all import ARP, Ether, srp

def scan_local_network(target_ip):
    # Create ARP request packet
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast
    packet = ether / arp

    print(f"[i] Scanning {target_ip}...")

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices

def display_result(devices):
    print("Available devices in the network:")
    print("IP" + " "*18 + "MAC")
    print("-" * 40)
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))

# Example: Change to match your subnet
target_subnet = "192.168.1.0/24"

devices = scan_local_network(target_subnet)
display_result(devices)