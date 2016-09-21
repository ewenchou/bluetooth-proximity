# Bluetooth Proximity Detection

Python code for getting the RSSI value of a Bluetooth device by address. Based on the value returned, can determine the proximity of the device.

This code was adapted from [this Github](https://github.com/dagar/bluetooth-proximity) by Daniel Agar.

## Requirements

This code requires the `bluetooth` and `python-bluez` modules to be installed. On Ubuntu/Debian systems, this can usually be done with the following commands:

        sudo apt-get install bluetooth
        sudo apt-get install python-bluez

*Note: Your system must also have a Bluetooth adapter.*

## Installation

```
git clone https://github.com/ewenchou/bluetooth-proximity.git
cd bluetooth-proximity
sudo python setup.py install
```

## Test

A simple test script is available in the `tests` directory that will output the RSSI value of a Bluetooth address. 

                python test_address.py <bluetooth-address> [number-of-requests]

This can be used to test if the code is working on your setup and also to output the detected RSSI values as you move your Bluetooth device closer/further from the Bluetooth adapter.

## Notes

* The RSSI values returned will differ depending on your Bluetooth devices and your surroundings (e.g. are there walls/obstructions, multiple floors, etc). 
* Use the test script mentioned above to see what values are returned in your setup.
* RSSI values may be positive or negative integers. You can use the absolute value (i.e. always positive) if you see both.

