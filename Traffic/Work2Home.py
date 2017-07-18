#!/usr/bin/env python
import ssl
import simplejson, urllib
import gpiozero
from pushbullet import Pushbullet

#Pushbullet setup
api_key = open('/home/pi/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
#print api_key
pb = Pushbullet(api_key) 

context = ssl._create_unverified_context()
origin = open('/home/pi/RouterPi/Traffic/work.config', 'r').read()
destination = open('/home/pi/RouterPi/Traffic/home.config', 'r').read()
apikey = open('/home/pi/RouterPi/Traffic/MapsAPI.config', 'r').read()
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
dt3 = "ETA to home is %d Minutes" % (dt2)

if dt2 <= 35:
	print "good"
	TravelString = "The Traffic is Good, ETA: %d Minutes" % (dt2)
	push = pb.push_note(dt3, TravelString)
elif dt2 >= 36 or dt2 <= 40:
	print "moderate"
	TravelString = "The Traffic is Moderate, ETA: %d Minutes" % (dt2)
	push = pb.push_note(dt3, TravelString)
else:
	print "heavy"
	TravelString = "WTF Traffic is a nightmare!!!, ETA: %d Minutes" % (dt2)
	push = pb.push_note(dt3, TravelString)
