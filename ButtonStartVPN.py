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
	os.system("/home/pi/TorrentVPN.sh") #If button pressed shutdown pi
        break
    time.sleep(1)
