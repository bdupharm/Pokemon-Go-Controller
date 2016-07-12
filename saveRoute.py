import xml.etree.cElementTree as ET
import urllib2
import json
import time
import socket
import signal
import sys

lastLat = ""
lastLng = ""
path = open("path.csv", "wb")


def getPokemonLocation():
	try:
                response = urllib2.urlopen("http://10.11.12.233:8080/", timeout = 1)
		return json.load(response)
	except (urllib2.URLError, socket.timeout) as e:
                print "Likely, timout. Connecting Again"
                getPokemonLocation()


def generateXML():
        global lastLat, lastLng, path

	geo = getPokemonLocation()
	if geo != None:
		if geo["lat"] != lastLat or geo["lng"] != lastLng:
                        lastLat = geo["lat"]
                        lastLng = geo["lng"]
                        path.write("{},{}\n".format(geo["lat"], geo["lng"]))
			print "Location Updated!", "latitude:", geo["lat"], "longitude:" ,geo["lng"]


def signal_handler(sig, frame):
    print "Closing app"
    path.close()
    sys.exit()


def start():
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        generateXML()


start()
