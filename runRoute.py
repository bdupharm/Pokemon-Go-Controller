#!/usr/bin/env python

import xml.etree.cElementTree as ET
import random
import csv
import signal
import sys
import time

random.gauss(40.7537749210475, 0.00001)


reader = csv.reader(open("pathOne.csv", "rU"))

def signal_handler(sig, frame):
    print "Closing app"
    sys.exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        for row in reader:
            lat = random.gauss(float(row[0]), 0.00001)
            lng = random.gauss(float(row[1]), 0.00001)

            # sleep a random time btwn 1 - 3 secs
            time.sleep(random.uniform(1, 2))

            gpx = ET.Element("gpx", version="1.1", creator="Xcode")
            wpt = ET.SubElement(gpx, "wpt", lat=str(lat), lon=str(lng))
            ET.SubElement(wpt, "name").text = "PokemonLocation"
            ET.ElementTree(gpx).write("pokemonLocation.gpx")
            print "Location Updated!", "latitude:", lat, "longitude:" ,lng
