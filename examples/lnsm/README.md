# Log Normal Shadowing Model
Python code for getting the static distance between bluetooth devices using the RSSI value.

RSSI is measured in dBm but is in its raw form not really useful in an application (apart from being a diagnostic measurement). 
The nice thing about RSSI is that we can translate the measurements to distance estimates in meters or centimeters. 
We can describe the relation between RSSI and distance using a model, the Log Normal Shadowing Model/ Log Distance Pathloss Model.

### x = (RSSI_value-A0)/(-10*n)        
### distance = ((10^x) * 100) + c

A0 = Average RSSI value measured at a distance of 1m from  the transmitting device.

n = Signal Propagation Exponent. It is a constant that differs from environment to environment (0<n<5).

c = Environment Constant. It is a weight added to the distance inorder to reduce the error. It is a constant that differs from environment to environment.

actual_dist = The static distance between the two bluetooth devices during measurement. This value is equal to the distance between the bluetooth devices. E.g: If the distance between the two devices is 20cm, the actual_dist = 20.

You must first measure the avearge value of RSSI(A0) at 1m from the device. After this you must adjust the values of n & c to reduce the error.
In the example, the values of A0,n & c have been configured to work with a Motorola G4 Plus as the measured bluetooth device. Hence depending upon the bluetooth device being measured, the values of A0,n & c will change respectively.

Following our model, in an ideal world, the RSSI value is only dependent on the distance between the two devices.
In reality, however, RSSI values are heavily influenced by the environment and have, consequently, high levels of noise. This noise is, for example, caused by multi-path reflections: signals bounce against objects in the environment such as walls and furniture.
So, we need to fight the noise. Here Kalman filters come in to play. The Kalman filter is a state estimator that makes an estimate of some unobserved variable based on noisy measurements.
