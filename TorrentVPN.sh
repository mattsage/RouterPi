OldIP=`wget http://ipinfo.io/ip -qO -`
echo "****************************************"
echo $OldIP
echo "****************************************"
cd /etc/openvpn/
sudo service transmission-daemon reload 
sudo openvpn --config /etc/openvpn/UK\ Southampton.ovpn --auth-user-pass /etc/openvpn/login.txt &
sleep 5
yes "" | echo "VPN Connected"
NewIP=`wget http://ipinfo.io/ip -qO -`
echo "****************************************"
echo $NewIP
echo "****************************************"
gpio mode 14 out
gpio write 14 1
