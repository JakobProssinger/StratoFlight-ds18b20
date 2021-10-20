#!/usr/bin/python3
# main.py - Temperatur Messung 
import os, sys, time

def getTemperatur(deviceAdresses):

# 1-wire Slave Datei lesen
	temperature = [0.0] * len(device_adresses)
	counter = 0
	for address in deviceAdresses:
		#Sensoren auslesen 
		try:
			file = open('/sys/bus/w1/devices/' + address + '/w1_slave')
		except OSError:
			print('cannot open', ('/sys/bus/w1/devices/' + address + '/w1_slave'))
			temperature[counter] = 'Error'
			counter= counter + 1 
		else:					
			filecontent = file.read()
			file.close()

			# Error in Temperatursensor Daten
			if len(filecontent) != 75:
				print("File Error")
			else :
				stringvalue = filecontent.split("\n")[1].split(" ")[9]
				temperature[counter] = float(stringvalue[2:]) / 1000
				counter = counter + 1 

	return temperature

if __name__ == '__main__':
	device_adresses = ['28-00000cdfc36f', '28-00000cdf6b81']
	for i in range (0, 10 ,1):
		time.sleep(1)
		print(getTemperatur(device_adresses))
