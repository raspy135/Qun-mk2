# Battery operation

## WARNING: 

This is for advanced users who is familiar with soldering. No warranty when the unit is broken by the modification. (I can answer questions on Discord)

Also, this is experimental state. I'm seeing unstability when the battery goes low state.

## Summary:

The base board (ESP32 Lyrat) has a Lipo charger circuit and the JST PH connector for Lipo battery. Thus you can connect Lipo to the base board for the battery operations. There are some limitations such as no battery status information.

## Parts list:

 - Lipo battery : Select Lipo battery with safety circuit to avoid over discharge(When you see any circuit in the Lipo that's it). I use 2000mah https://a.co/d/3RQlaXL
 - 100uF 5.0V+ capacitor. Lipo battery is sometimes weak and it might cause SD card writing issue. In order to avoid this, you need to add one capacitor between the power line. You can use generic one.
 - SPST Switch: A generic SPST Switch.

## Schematic

![battery_schematic](/Users/ryosukekojima/git/Qun-mk2/manual_images/battery_schematic.png)

## Steps to install

1. Remove bottom board.

2. Trim spiky button legs to protect Lipo.  Optionally you want to cut the switch on the board to make a room for Lipo(You don't need the main switch of the base board, it's always ON).

3. Check the polarity of Lipo battery.  ***There is no standard Polarity for Lipo battery!!!***  . Check the polarity signs (+ and -) on the base board. If you purchase the lipo that has wrong polarity, just remove the plastic piece on the board and flip it. The part is flippable.

   ![battery_connector](/Users/ryosukekojima/git/Qun-mk2/manual_images/battery_connector.jpg)

4. Solder Capacitor to the bottom of UART port

   ![capacitor_soldering](/Users/ryosukekojima/git/Qun-mk2/manual_images/capacitor_soldering.png)
   
5. Solder battery and switch

   ![switch_soldering](/Users/ryosukekojima/git/Qun-mk2/manual_images/switch_soldering.png)
   
6. Glue switch to the board, and install the battery between the base board and the main circuit board. Don't short the circuit.
7. Assemble the unit and test.

## Operations

- When the switch is OFF, you can use USB as a power source.
- When the switch is ON, Battery will be used as a power source AND USB will charge the battery. However, the unit might be not stable when the battery is very low capacity. Switch off when it is not stable.
- To charge, turn the switch to ON and connect USB cable. Extra red LED on the base board will be lit. It changes green when the charge is finished.
- Always turn off the switch when you connect or disconnect USB cable.
- When the battery goes empty, the synth will hang. Display is still on, but no  more power to run synth engine. Charge the battery to recover.