import ssl
import simplejson, urllib
import gpiozero
context = ssl._create_unverified_context()
origin = open('/home/pi/RouterPi/work.config', 'r').read()
destination = open('/home/pi/RouterPi/home.config', 'r').read()
apikey = open('/home/pi/RouterPi/MapsAPI.config', 'r').read()
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

if dt2 <= 35:
	print "good"
elif dt2 >= 36 or dt2 <= 40:
	print "moderate"
else:
	print "heavy"
