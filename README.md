# Triggered Waveform Data Acquisiton (DAQ) Script for MDO4034C

Tektronix MDO4034C oscilloscope can only save waveforms in manual mode. By manually pressing a button on the front panel or in the web interface. The goal of this project is to allow waveform acquisition upon the trigger event of the oscilloscope.

Desired logic can be implemented by means of controlling the oscilloscope by a host computer. Due to certain security issues, Windows operating systems are not favored by the JLab IT department. Therefore Brad installed Red Hat Enterprise Linux (RHEL) v8.5.

## Prerequisites
* Configure a linux-based PC with internal LAN. Two network cards are required to access the internet and intranet.
* Install the National Instruments [(NI) VISA software](https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html) drivers.
https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html
* Install a Python IDE (e.g. Wing) for debugging capabilities.
* Establish a connection between the host computer and the scope by means of the [PyVisa library](https://pyvisa.readthedocs.io/en/latest/). 
* Utilize MDO4034C Programming Manual to implement the desired logic.
