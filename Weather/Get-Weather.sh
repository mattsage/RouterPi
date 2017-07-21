#!/usr/bin/env bash

##################################
#Name: GetWeather.sh
#Author: Matthew Sage
#Latest Update: 21/07/17
#Fetches Daily Weather from WeatherUnderground
##################################

#Script ot be ran at 6am daily via cron job
#crontab -e
# 00 06 * * * /home/pi/RouterPi/Weather/Get-Weather.sh

apikey=`cat /home/pi/APIConfigs/WUapikey.config` #Get WeatherUnderground API key from apikey.config
location=`cat /home/pi/APIConfigs/WUlocation.config`

pywu fetch $apikey $location #Outputs File to /tmp/pywu.cache.json
