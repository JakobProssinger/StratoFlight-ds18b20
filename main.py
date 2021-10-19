
#!/usr/bin/python
# main.py - Temperatur Messung 
import os, sys, time

device_adress = '28-000005d2e508'

def aktuelleTemperatur():

    # 1-wire Slave Datei lesen
    file = open('/sys/bus/w1/devices/'+ device_adress + 'w1_slave')
    filecontent = file.read()
    file.close()

    # Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000

    # Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature 
    return(rueckgabewert)

