#!/bin/bash

################################################################################################################################################################################
# Author: Matthew Sage                                  				                               							       #
# Date: 17/07/2017																			       #																			   #
# Description: Script is run soon as button StartVPN.py is pressed. Connects to VPN, starts Transmission, sends IPs to Pushbullet, Light LED (GPIO #14), executes Shutdown.py  #
################################################################################################################################################################################

OldIP=`wget http://ipinfo.io/ip -qO -`
echo "****************************************"
echo $OldIP
echo "****************************************"
cd /etc/openvpn/
#sudo service transmission-daemon reload 
sudo service deluged start
deluge-web &
sudo openvpn --config /etc/openvpn/UK\ Southampton.ovpn --auth-user-pass /etc/openvpn/login.txt &
sleep 5
yes "" | echo "VPN Connected"
NewIP=`wget http://ipinfo.io/ip -qO -`
echo "****************************************"
echo $NewIP
echo "****************************************"

gpio mode 14 out

if [ $OldIP = $NewIP ]
then
	echo "VPN Failed to connect"
	/usr/bin/Pushbullet.sh "VPN Failed to connect"
	blink=1
	while [ $blink -le 20 ]
	do
		#gpio mode 14 out
		gpio write 22 1
		sleep 1
		gpio write 22 0
		(( blink++ ))
		break
	done
else
	/usr/bin/Pushbullet.sh "Old IP: $OldIP New IP: $NewIP"
	#gpio mode 14 out
	gpio write 22 1
	sudo python /home/pi/RouterPi/Shutdown.py
fi
