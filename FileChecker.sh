#!/bin/bash

###################################################################################################
# Author: Matthew Sage                                  				                               		#																                                             #
# Date: 17/07/2017																																			          #                                                                    			   #
# Description: Checks file location for finished downloads, once complete LED on GPIO ??? is lit  #
###################################################################################################
#!/bin/bash
foldercount=`ls /home/pi/Downloads/ -1 | wc -l`

while [ $foldercount != 0 ]
do
	echo "$foldercount files left"
	sleep 5m #Sleep for 5 Mins
	foldercount=`ls /home/pi/Downloads/ -1 | wc -l`
done

echo "No Files left"
