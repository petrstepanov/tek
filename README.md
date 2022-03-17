# Triggered Waveform Data Acquisiton (DAQ) Script for MDO4034C

<img width="100%" src="https://github.com/petrstepanov/tek/blob/main/resources/connectivity-diagram.png?raw=true" alt="Tektronix MDO4034C connectivity diagram with NAS"/>

Tektronix MDO4034C oscilloscope can only save waveforms in manual mode. By manually pressing a button on the front panel or in the web interface. The goal of this project is to allow waveform acquisition upon the trigger event of the oscilloscope.

Desired logic can be implemented by means of controlling the oscilloscope by a host computer. Due to certain security issues, Windows operating systems are not favored by the JLab IT department. Therefore Brad installed Red Hat Enterprise Linux (RHEL) v8.5.

## Prerequisites
* Configure a linux-based PC with internal local area network (LAN). Two network cards are required to access the internet and intranet.
* Plug-in computer, oscillscope and the network attached storage (NAS) into the switch on the LAN.
* Install the National Instruments [(NI) VISA software](https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html) drivers.
https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html
* Install a Python IDE (e.g. Wing) for debugging capabilities.
* Establish a connection between the host computer and the scope by means of the [PyVisa library](https://pyvisa.readthedocs.io/en/latest/). 
* Set up SAMBA service on the NAS. Enable SMB1 protocol in the NAS settings (required by the scope).
* In the oscilloscope settings mount shared SAMBA NAS drive as letter I:
* [MDO4034C Programming Manual](https://download.tek.com/manual/MDO4000-B-C-MSO-DPO4000B-and-MDO3000-Oscilloscope-Programmer-Manual-077051007.pdf) is utilized to implement the desired logic. Script to be used is `test.py`.

## Resources
A [few useful examples](https://forum.tek.com/viewtopic.php?f=580&t=133570) was referred by a Tektronix developer [Steve Guerrero](mailto:steve.guerrero@tektronix.com). However examples are for different oscilloscope models and written in Python v.2 (not v.3).
