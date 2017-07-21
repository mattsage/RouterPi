#!/usr/bin/env python

#########################################################################################################################
# Author: Matthew Sage                                  				                                #
# Date: 18/07/2017													#
# Description: Traffic ETA with LED Status and Pushbullet Notification							#
# Crontab -e: 45 5 * * 1-5 python /home/pi/RouterPi/Traffic/TrafficTimes.py 						#
#########################################################################################################################

import datetime
import ssl
import simplejson, urllib
from gpiozero import LED
from pushbullet import Pushbullet
from time import sleep

#LED Setup
#Rled = LED(17)
#Oled = LED(17)
#Gled = LED(17)

#Pushbullet setup
api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
#print api_key
pb = Pushbullet(api_key) 


now = datetime.datetime.now()
if now.hour < 12:
  print "Morning"
  origin = open('/home/pi/RouterPi/Traffic/home.config', 'r').read()
  destination = open('/home/pi/RouterPi/Traffic/work.config', 'r').read()
  trafficLoc = "Work"
  #print origin
  #print destination
  print "Going to %s" % (trafficLoc)
else:
  print "Evening"
  origin = open('/home/pi/APIConfigs/work.config', 'r').read()
  destination = open('/home/pi/APIConfigs/home.config', 'r').read()
  trafficLoc = "Home"
  #print origin
  #print destination
  print "Going %s" % (trafficLoc)

context = ssl._create_unverified_context()
apikey = open('/home/pi/APIConfigs/MapsAPI.config', 'r').read()
traffic = "best_guess"
#best_guess, pesimistic, optimistic
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&traffic_model="+traffic+"&departure_time=now&origins="+origin+"&destinations="+destination+"&mode=driving&language=en-EN&sensor=false&key="+apikey
result= simplejson.load(urllib.urlopen(url, context=context))
#print (result)
driving_time = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
#print driving_time
#with open("test.txt", "a") as myfile:
#    myfile.write("Time: %s" % driving_time)
dt2 = int(filter(str.isdigit, driving_time))
print dt2
dt3 = "ETA to %s is %d Minutes" % (trafficLoc, dt2)

if dt2 <= 35:
	print "Good"
	TravelString = "The Traffic is Good, ETA: %d Minutes" % (dt2)
	push = pb.push_note(dt3, TravelString)
  	if trafficLoc == "Work":
        	print "GLED ON"
		#Gled.on()
        	#sleep(1800)
		#Gled.off()
elif dt2 >= 36 or dt2 <= 40:
	print "Moderate"
	TravelString = "The Traffic is Moderate, ETA: %d Minutes" % (dt2)
	push = pb.push_note(dt3, TravelString)
  	if trafficLoc == "Work":
		print "OLED ON"
		#Oled.on()
        	#sleep(1800)
        	#Oled.off()
else:
	print "Heavy"
	TravelString = "WTF Traffic is a nightmare!!!, ETA: %d Minutes" % (dt2)
	push = pb.push_note(dt3, TravelString)
  	if trafficLoc == "Work":
        	print "RLED ON"
		#Rled.on()
        	#sleep(1800)
        	#Rled.off()
