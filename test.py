# Import PyVISA library
import pyvisa
#import usb
import matplotlib
import numpy

# Docs here: https://pyvisa.readthedocs.io/en/latest/index.html
pyvisa.log_to_screen()

# Create Resource Manager object with default IVI backend (no arguments)
#rm = pyvisa.ResourceManager()
#rm.list_resources()
#print(rm.list_resources('?*'))
#print(rm.list_resources())

#ipaddr = 'TCPIP:192.168.100.36::INSTR'
#inst = rm.open_resource(ipaddr)

# Create Resource Manager with Py backend
rmpy=pyvisa.ResourceManager('@py')
rmpy.list_resources()

# print(rmpy.list_resources('TCP?*'))
# print(rmpy.list_resources())

# Issue: Found a device whose serial number cannot be read
# Solution: https://www.google.com/search?client=firefox-b-1-e&q=pyvisa+Found+a+device+whose+serial+number+cannot+be+read

ipaddr = 'TCPIP::192.168.100.36::INSTR'
inst = rmpy.open_resource(ipaddr)

print(inst.query('*IDN?'))

values = inst.query_ascii_values('CURV?', container=numpy.array)

print(values)

plot = matplotlib.pyplot.plot(values)