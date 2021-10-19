## Pin Blegeung des ds18b20:

    ------------
    \ 1  2  3 /
     \_______/  
    1: GND
    2: DQ - Daten Leitung
    3: VDD - Versorgung Spannung 3 - 5.5V 

## Schaltungssaufbau:
    VDD an Pin 1            -   3,3V
    DQ  an Pin 7 (GPIO4)    -   kann allerdings frei gewählt werden 
    GND an Pin 9            -   Masse

    Zwischen **DQ** und **VDD** wird ein **Widerstand R1** Parallel geschalten. 