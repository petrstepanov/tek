# Install packages on RHEL 8.5 with: pip3.9 install ...
# because nivisa requires python version > ...
import pyvisa
import matplotlib
import numpy
# import usb

# Docs here: https://pyvisa.readthedocs.io/en/latest/index.html
pyvisa.log_to_screen()

# NOT WORKING
# Create Resource Manager object with default IVI backend (no arguments)
# rm = pyvisa.ResourceManager()
# rm.list_resources()
# print(rm.list_resources('?*'))
# print(rm.list_resources())

# WORKS
# Create Resource Manager with Py backend
rmpy=pyvisa.ResourceManager('@py')

# NOT WORKING
# USB issue: Found a device whose serial number cannot be read
# Potential solution: https://www.google.com/search?client=firefox-b-1-e&q=pyvisa+Found+a+device+whose+serial+number+cannot+be+read
# print(rmpy.list_resources())

# WORKS
# Ethernet approach: https://github.com/pyvisa/pyvisa-py/issues/261
ipaddr = 'TCPIP::192.168.100.36::INSTR'
inst = rmpy.open_resource(ipaddr)
print(inst.query('*IDN?'))

# TEST: acquire waveform from the scope and plot
values = inst.query_ascii_values('CURV?', container=numpy.array)
print(values)
plot = matplotlib.pyplot.plot(values)
