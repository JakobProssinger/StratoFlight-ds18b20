#!/usr/bin/python
# main.py - Temperatur Messung 
import os, sys, time

def getTemperatur(deviceAdresses):

# 1-wire Slave Datei lesen
	filecontent = ""
	for adress in deviceAdresses:
		try:
			file = open('/sys/bus/w1/devices/' + adress + '/w1_slave')
			break
		except OSError:
			print('cannot open', ('/sys/bus/w1/devices/' +adress + '/w1_slave'))
			return  0.0
	filecontent = 	file.read()
	file.close()

	# Temperaturwerte auslesen und konvertieren
	stringvalue = filecontent.split("\n")[1].split(" ")[9]
	temperature = float(stringvalue[2:]) / 1000

	# Temperatur ausgeben
	rueckgabewert = '%6.2f' % temperature 
	return(rueckgabewert)

if __name__ == '__main__':
	device_adresses = ['28-00000cdfc36f', '28-00000cdf6b81']
	for i in range (0, 10 ,1):
		time.sleep(1)
		print(getTemperatur(device_adresses))
