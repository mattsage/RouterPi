# RouterPi
Transmission, VPN and Pi-Hole

Sofware to install:
Transmission
OpenVPN
Pi-Hole

Scripts Description
StartVPN.py	- Script is run at boot. Waits for button on GPIO #17 to be pressed. Once Pressed TorrentVPN.sh is executed
TorrentVPN.sh - Script is run soon as button StartVPN.py is pressed. Connects to VPN, starts Transmission, sends IPs to Pushbullet, Light LED (GPIO #14), executes Shutdown.py
Shutdown.py	- Python Script which runs after TorrentVPN.sh. Configured button on GPIO #17 to shutdown the Pi. Can be set up via: https://github.com/mattsage/Shutdown-Button
FileChecker.sh - Checks file location for finished downloads, once complete LED on GPIO ??? is lit
Pushbullet.sh - Pushbullet notification of new IP address when VPN is turned on. 
WhatsMyIP.sh - Script used to output external IP address

GPIOs Used
#17 - Button
#14 - LED for VPN Connected
