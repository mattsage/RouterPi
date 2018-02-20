from gpiozero import LED
from time import sleep

Gled = LED(25)
Oled = LED(23)
Rled = LED(27)
BOled = LED(22)
BGled = LED(24)

while True:
    Gled.on()
    print "Green LED ON!"
    sleep(5)
    Gled.off()
    Oled.on()
    print "Orange LED ON!"
    sleep(5)
    Oled.off()
    Rled.on()
    print "RED LED ON!"
    sleep(5)
    Rled.off()
    BOled.on()
    print "Bottom Orange LED ON!"
    sleep(5)
    BOled.off()
    BGled.on()
    print "Bottom Green LED ON!"
    sleep(5)
    BGled.off()
