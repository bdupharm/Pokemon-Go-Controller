import os
import urllib2
import json
import time
import socket

def checkConnected():
	try:
		response = urllib2.urlopen("http://10.11.12.233:8080/", timeout = 1)
		return json.load(response)
	except (urllib2.URLError, socket.timeout) as e:
		print "Likely timeout, trying again"
                checkConnected()

def clickAction():
	os.system("./autoClicker -x 800 -y 610")
	time.sleep(.2)
	os.system("./autoClicker -x 800 -y 660")
	os.system("./autoClicker -x 250 -y 700")
	time.sleep(2)
	print "clicking!!"

def start():
	while True:
		if checkConnected() != None:
			clickAction()

start()
