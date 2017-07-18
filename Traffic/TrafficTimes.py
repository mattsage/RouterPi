#!/usr/bin/env python

#########################################################################################################################
# Author: Matthew Sage                                  				                                #
# Date: 18/07/2017													#
# Description: Traffic ETA from Home to Work With LED Status and Pushbullet Notification				#
# Crontab -e: 45 5 * * 1-5 python /home/pi/RouterPi/Traffic/Home2Work.py 						#
#########################################################################################################################

import datetime
import ssl
import simplejson, urllib
from gpiozero import LED
from pushbullet import Pushbullet
from time import sleep

timenow = datetime.datetime.time(datetime.datetime.now())

print timenow
