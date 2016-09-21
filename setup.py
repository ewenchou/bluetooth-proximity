from setuptools import setup, find_packages

setup(name='bt_proximity',
    version='0.1',
    description="Detects if a Bluetooth device is near by querying its RSSI value",
    url='',
    author='Ewen Chou',
    author_email='ewenchou@gmail.com',
    license='Apache 2.0',
    packages=find_packages(),
    zip_safe=False)
