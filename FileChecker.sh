#!/bin/bash

###################################################################################################
# Author: Matthew Sage                                  				                               		#																                                             #
# Date: 17/07/2017																																			          #                                                                    			   #
# Description: Checks file location for finished downloads, once complete LED on GPIO ??? is lit  #
###################################################################################################
#foldercount=`ls -1 | wc -l`
foldercount=`ls /home/pi/Downloads/ -1 | wc -l`

while [ $foldercount != 0 ]
do
	echo "$foldercount files left"
	sleep 15
#	foldercount=`ls -1 | wc -l`
	foldercount=`ls /home/pi/Downloads/ -1 | wc -l`
	find /home/pi/Downloads -name "*.torrent" -type f -delete
done

echo "No Files left"
