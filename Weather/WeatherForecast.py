#!/usr/bin/env python

#########################################################################################################################
# Author: Matthew Sage                                                          				                                #
# Date: 21/07/2017				                                                                            									#
# Description: Weather Report on Condition and High/Low Temps                                                  	  			#
#########################################################################################################################
import subprocess
from pushbullet import Pushbullet

#Pushbullet setup
api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
pb = Pushbullet(api_key) 

#Get Weather Condition
condition = subprocess.check_output("pywu forecast condition", shell=True)
condition = condition.replace("\n", "")
#Get Temp Low
low = subprocess.check_output("pywu forecast low_c", shell=True)
low = low.replace("\n", "")
low = low + "C"
#Get Temp High
high = subprocess.check_output("pywu forecast high_c", shell=True)
high = high.replace("\n", "")
high = high + "C"

forecast = "Forecast today is %s, with highs of %s and lows of %s" % (condition,high,low)
print forecast
push = pb.push_note(condition, forecast)
