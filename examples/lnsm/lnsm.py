from bt_proximity import BluetoothRSSI
import time
import sys
import math

BT_ADDR = ''  # You can put your Bluetooth address here.  E.g: 'a4:70:d6:7d:ee:00'
NUM_LOOP = 30

def print_usage():
    print("Usage: python test_address.py <bluetooth-address> [number-of-requests]")


def main():
    if len(sys.argv) > 1:
        addr = sys.argv[1]
    elif BT_ADDR:
        addr = BT_ADDR
    else:
        print_usage()
        return
    if len(sys.argv) == 3:
        num = int(sys.argv[2])
    else:
        num = NUM_LOOP
    btrssi = BluetoothRSSI(addr=addr)

    n=1.5    #Path loss exponent(n) = 1.5
    c = 10   #Environment constant(C) = 10
    A0 = 2   #Average RSSI value at d0
    actual_dist = 37   #Static distance between transmitter and Receiver in cm
    sum_error = 0
    count = 0

    for i in range(1, num):
        rssi_bt = float(btrssi.get_rssi())
        if(rssi_bt!=0 and i>10):                    #reduces initial false values of RSSI using initial delay of 10sec
            count=count+1
            x = float((rssi_bt-A0)/(-10*n))         #Log Normal Shadowing Model considering d0 =1m where
            distance = (math.pow(10,x) * 100) + c
            error = abs(actual_dist - distance)
            sum_error = sum_error + error
            avg_error = sum_error/count
            print("Average Error=  " + str(avg_error))
            print("Error=  " + str(error))
            print("Approximate Distance:" + str(distance))
            print("RSSI: " + str(rssi_bt))
            print("Count: " + str(count))
            print(" ")
        time.sleep(1)




if __name__ == '__main__':
    main()

