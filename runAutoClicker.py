import os
import urllib2
import json
import time
import socket

lastLat = ""
lastLng = ""


def checkConnectedAndLocationChanged():
    global lastLat, lastLng
    try:
        response = urllib2.urlopen("http://10.11.12.233:8080/", timeout = 1)
        geo = json.load(response)
        if geo["lat"] != lastLat or geo["lng"] != lastLng:
            lastLat = geo["lat"]
            lastLng = geo["lng"]
            # MAKE CLICK ACTION
            return True
        # IF LOCATION DIDNT CHANGE DONT DO SHIT
        return False
    except (urllib2.URLError, socket.timeout) as e:
        print "Likely timeout, trying again"
        checkConnectedAndLocationChanged()

def clickAction():
    # Click to update location on device
    os.system("./autoClicker -x 800 -y 610")
    time.sleep(.05)
    #time.sleep(.2)
    os.system("./autoClicker -x 800 -y 660")
    print "clicking!!"

    ## Click back to simulator
    #os.system("./autoClicker -x 300 -y 770")
    #time.sleep(2)

def start():
    while True:
        if checkConnectedAndLocationChanged():
            clickAction()

start()
