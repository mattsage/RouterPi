#!/bin/bash

########################################################################################
# Author: Matthew Sage                                            									   #
# Date: 17/07/2017		                                															   #
# Description: Does internet Speed Test                                                #
########################################################################################

date >> /home/pi/RouterPi/speedtest.log
/usr/local/bin/speedtest --simple >> /home/pi/speedtest.log
