#!/usr/bin/env python

#########################################################################################################################
# Author: Matthew Sage                                  				                                #
# Date: 17/07/2017													#
# Description:Script is run at boot. Waits for button on GPIO #17 to be pressed. Once Pressed TorrentVPN.sh is executed #				#
#########################################################################################################################

import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP) #setup GPIO pin #17 as Pull up down
GPIO.setup(27,GPIO.OUT)
while True:
    print GPIO.input(17)
    if(GPIO.input(17) == False):
        GPIO.output(27,GPIO.HIGH)
	os.system("/home/pi/RouterPi/TorrentVPN.sh") #If button pressed shutdown pi
        break
    time.sleep(1)
