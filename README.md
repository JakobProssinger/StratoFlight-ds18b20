## Pin Belegung des ds18b20:

    (Ansicht von Unten)
    ------------
    \ 1  2  3 /
     \_______/  
    1: GND
    2: DQ - Daten Leitung
    3: VDD - Versorgungs-Spannung 3 - 5.5V 

## Schaltungssaufbau:
    VDD an Pin 1            -   3,3V
    DQ  an Pin 7 (GPIO4)    -   kann allerdings frei gewählt werden 
    GND an Pin 9            -   Masse

    An DQ wird ein Pull-Up Widerstand R1 mit 3,3kΩ bist 4,7kΩ angeschlossen.

## One-Wire Setup
    Um 1-Wire zu aktivieren muss ein der device tree (dt) erweitert werden, damit die Module geladenwerden.
    Dazu muss in /boot/config.txt folgende Zeile eingefügt werden:
```
dtoverlay=w1-gpio,gpiopin=4
```
    Statt GPIO-Pin 4 können beliebige GPIO Pins gewählt werden.

    Nach einem reboot werden die One-Wire Slaves gefunden. Die Adressen und Daten können im Ordner /sys/bus/w1/devices/ gefunden werden.
    Source: "pinout.xyz/pinout/1_wire"
