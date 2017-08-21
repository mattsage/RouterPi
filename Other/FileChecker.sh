#!/bin/bash
#foldercount=`ls -1 | wc -l`
#/home/pi/ConnectRAID.sh
sleep 5m

foldercount=`ls /home/pi/Downloads/ -1 | wc -l`

while [ $foldercount != 0 ]
do
	echo "$foldercount files left"
	sleep 1m
#	foldercount=`ls -1 | wc -l`
	foldercount=`ls /home/pi/Downloads/ -1 | wc -l`
	find /home/pi/Downloads -name "*.torrent" -type f -delete
done

echo "No Files left"
#sudo mv /home/pi/CompletedDLs/* /mnt/RAID-NAME/
/usr/bin/Pushbullet.sh "Downloads Completed"
sudo /home/pi/blink1/commandline/blink1-tool --green
