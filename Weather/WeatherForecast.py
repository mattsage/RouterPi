#!/usr/bin/env python

#########################################################################################################################
# Author: Matthew Sage                                                          				                                #
# Date: 21/07/2017				                                                                            									#
# Description: Weather Report on Condition and High/Low Temps                                                  	  			#
#########################################################################################################################
import subprocess
import datetime
from pushbullet import Pushbullet

#Pushbullet setup
api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
pb = Pushbullet(api_key) 

subprocess.call("/home/pi/RouterPi/Weather/Get-Weather.sh", shell=True)

#Date
datetoday = datetime.datetime.now().strftime('%A %d %B') #Todays Date e.g. Monday 13 June

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
#Get Rain mm
rain = subprocess.check_output("pywu forecast rain_mm", shell=True)
rain = rain.replace("\n", "")
rain = rain + "mm"

pbsubject = "%s Today! High of %s" % (condition,high)
forecast = "The forecast for %s is %s, with highs of %s and lows of %s. You will have %s of rain" % (datetoday,condition,high,low,rain)

push = pb.push_note(pbsubject,forecast)
