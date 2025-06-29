import subprocess
from pystyle import Colorate, Colors

ip = " Input the ip -> "

Ip_Color = Colorate.Horizontal(Colors.blue_to_purple, ip)
ip = input(Ip_Color)
subprocess.run(f"ping " + ip)
input("press enter to complete...")

#Cyssym
