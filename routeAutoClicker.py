import os
import time

def clickAction():
    # Click to update location on device
    os.system("./autoClicker -x 800 -y 610")
    time.sleep(1)
    #time.sleep(.2)
    os.system("./autoClicker -x 800 -y 660")
    print "clicking!!"

if __name__ == "__main__":
    while True:
        clickAction()
