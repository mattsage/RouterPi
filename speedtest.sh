#!/bin/bash

date >> /home/pi/speedtest.log
/usr/local/bin/speedtest --simple >> /home/pi/speedtest.log
