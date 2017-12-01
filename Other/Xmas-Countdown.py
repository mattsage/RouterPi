import sys
import datetime
from pushbullet import Pushbullet

api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
#print api_key
pb = Pushbullet(api_key) 

dt = datetime.datetime.now()

month = datetime.date.today().strftime("%B") #Month e.g. June
#print month
daynumber = datetime.datetime.now().day 

mon = 12 - dt.month
day = 25 - dt.day
hr = 23 - dt.hour
mn = 60 - dt.minute
sec = 60 - dt.second

if month == "December" and daynumber < 25:
	s = repr(day) + 'days ' + repr(hr) + 'hours ' + repr(mn) + 'mins ' + repr(sec) + 'secs' + ' until Christmas'
	b = "Holidays are coming!"
	#print s
	push = pb.push_note(s, b)
elif month == "December" and daynumber == 25:
	s = "ITS CHRISTMAS!!!!!!!!!!"
	b = "Go and un-wrap some presents!!!"
	push = pb.push_note(s, s)
else:
	print ""
