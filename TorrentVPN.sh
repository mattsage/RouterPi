OldIP=`wget http://ipinfo.io/ip -qO -`
echo "****************************************"
echo $OldIP
echo "****************************************"
cd /etc/openvpn/
sudo service transmission-daemon reload 
sudo openvpn --config /etc/openvpn/UK\ Southampton.ovpn --auth-user-pass /et$
sleep 5
yes "" | echo "VPN Connected"
NewIP=`wget http://ipinfo.io/ip -qO -`
echo "****************************************"
echo $NewIP
echo "****************************************"
/usr/bin/Pushbullet.sh "Old IP: $OldIP New IP: $NewIP"
gpio mode 14 out
gpio write 14 1
