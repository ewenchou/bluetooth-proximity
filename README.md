# Bluetooth Proximity Detection

Python code for getting the RSSI value of a Bluetooth device by address. Based on the value returned, can determine the proximity of the device.

This code was adapted from [this Github](https://github.com/dagar/bluetooth-proximity) by Daniel Agar.

## Requirements

This code requires the `bluetooth` and `python-bluez` modules to be installed. On Ubuntu/Debian systems, this can usually be done with the following commands:

```
sudo apt-get install bluetooth
sudo apt-get install python-bluez
```

*Note: Your system must also have a Bluetooth adapter.*

## Installation

```
git clone https://github.com/ewenchou/bluetooth-proximity.git
cd bluetooth-proximity
sudo python setup.py install
```

## Examples

### test_address.py

This is a simple script to scan and output the RSSI value of a Bluetooth address in a loop. This can be used to test if the code is working on your setup and also to output the detected RSSI values as you move your Bluetooth device closer/further from the Bluetooth adapter.

Use `Ctrl + C` to exit the script or wait until number of loops has finished.

```
python test_address.py <bluetooth-address> [number-of-loops]
```

### bluetooth_scanner.py

An example script that uses threads to scan for bluetooth addresses in a loop and invokes a callback function when the RSSI value is within a specified threshold.

Edit the script and set the `BT_ADDR_LIST` variable to the list of bluetooth addresses to scan.

Use `Ctrl + C` to exit the script.

```
python bluetooth_scanner.py
```

### lnsm.py (Log Normal Shadowing Model)

An example script to scan & output the distance between two bluetooth devices using the RSSI value . The distance between the two devices is calculated using the Log-Normal Shadowing Model/Log-Distance Pathloss Model.

Use `Ctrl + C` to exit the script or wait until number of loops has finished. Recommended number of loops = 30

```
python lnsm.py <bluetooth-address> [number-of-loops]
```

## Notes

* The RSSI values returned will differ depending on your Bluetooth devices and your surroundings (e.g. are there walls/obstructions, multiple floors, etc). 
* Use the test script mentioned above to see what values are returned in your setup.
* RSSI values may be positive or negative integers. You can use the absolute value (i.e. always positive) if you see both.

