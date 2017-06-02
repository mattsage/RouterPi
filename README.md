# RouterPi
## Speed Test, Travel Times, Transmission, VPN and Pi-Hole  

### Sofware to install:  
1. git clone https://github.com/mattsage/RouterPi.git  
2. create /home/pi/Pushbulletkey.config  
3. git clone https://github.com/mattsage/Shutdown-Button.git  
4. Transmission - sudo apt-get install transmiassion  
5. OpenVPN -   
6. Pi-Hole - curl -sSL https://install.pi-hole.net | bash  

### Scripts Description  
1. ButtonStartVPN.py	- Script is run at boot. Waits for button on GPIO #17 to be pressed. Once Pressed TorrentVPN.sh is executed  
2. TorrentVPN.sh - Script is run soon as button StartVPN.py is pressed. Connects to VPN, starts Transmission, sends IPs to Pushbullet, Light LED (GPIO #14), executes Shutdown.py  
3. Shutdown.py	- Python Script which runs after TorrentVPN.sh. Configured button on GPIO #17 to shutdown the Pi. Can be set up via: https://github.com/mattsage/Shutdown-Button  
4. FileChecker.sh - Checks file location for finished downloads, once complete LED on GPIO ??? is lit  
5. Pushbullet.sh - Pushbullet notification of new IP address when VPN is turned on.   
6. WhatsMyIP.sh - Script used to output external IP address  

### GPIOs Used  
 #17 - Button  
 #14 - LED for VPN Connected  
 
