#!/usr/bin/env python
from bt_proximity import BluetoothRSSI
import datetime
import time
import threading
import requests
import sys

# List of bluetooth addresses to scan
BT_ADDR_LIST = []
DAILY = True  # Set to True to invoke callback only once per day per address
DEBUG = True  # Set to True to print out debug messages


def dummy_callback():
    print "Dummy callback function invoked"


def bluetooth_listen(
        addr, threshold, callback, sleep=1, daily=True, debug=False):
    """Scans for RSSI value of bluetooth address in a loop. When the value is
    within the threshold, calls the callback function.

    @param: addr: Bluetooth address
    @type: addr: str

    @param: threshold: Tuple of integer values (low, high), e.g. (-10, 10)
    @type: threshold: tuple

    @param: callback: Callback function to invoke when RSSI value is within
                      the threshold
    @type: callback: function

    @param: sleep: Number of seconds to wait between measuring RSSI
    @type: sleep: int

    @param: daily: Set to True to invoke callback only once per day
    @type: daily: bool

    @param: debug: Set to True to print out debug messages and does not 
                   actually sleep until tomorrow if `daily` is True.
    @type: debug: bool
    """
    b = BluetoothRSSI(addr=addr)
    while True:
        rssi = b.get_rssi()
        if debug:
            print "---"
            print "addr: {}, rssi: {}".format(addr, rssi)
        # Skip to next iteration if device not found
        if rssi is None:
            continue
        # Trigger if RSSI value is within threshold
        if threshold[0] < rssi < threshold[1]:
            callback()
            if daily:
                # Calculate the time remaining until next day
                now = datetime.datetime.now()
                tomorrow = datetime.datetime(
                    now.year, now.month, now.day, 0, 0, 0, 0) + \
                    datetime.timedelta(days=1)
                until_tomorrow = (tomorrow - now).seconds
                if debug:
                    print "Seconds until tomorrow: {}".format(until_tomorrow)
                else:
                    time.sleep(until_tomorrow)
        # Delay between iterations
        time.sleep(sleep)


def start_thread(addr, daily=True, debug=False):
    """Helper function that creates and starts a thread to listen for the
    bluetooth address.
    
    @param: addr: Bluetooth address
    @type: addr: str

    @param: daily: Daily flag to pass to `bluetooth_listen` function
    @type: daily: bool

    @param: debug: Debug flag to pass to `bluetooth_listen` function
    @type: debug: bool

    @return: Python thread object
    @rtype: threading.Thread
    """
    thread = threading.Thread(
        target=bluetooth_listen, 
        args=(), 
        kwargs={
            'addr': addr,
            'threshold': (-10, 10),
            'callback': dummy_callback,
            'sleep': 1,
            'daily': daily,
            'debug': debug
        }
    )
    # Daemonize
    thread.daemon = True
    # Start the thread
    thread.start()
    return thread


def main():
    if not BT_ADDR_LIST:
        print "Please edit this file and set BT_ADDR_LIST variable"
        sys.exit(1)
    threads = [start_thread(a, daily=DAILY, debug=DEBUG) for a in BT_ADDR_LIST]
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
