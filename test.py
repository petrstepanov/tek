# Install packages on RHEL 8.5 with: pip3.9 install ...
# because nivisa requires python version > ...
# echo 'set path = ($path /usr/local/bin $HOME/bin .)' >> ~/.login
import pyvisa
import matplotlib.pyplot as plt
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

# Configure the instrument
# https://pyvisa.readthedocs.io/en/latest/introduction/communication.html#getting-the-instrument-configuration-right
# p.2-5 Programmers manual: 
# | This oscilloscope does not support ASCII LF only message termination. The
# | oscilloscope always terminates outgoing messages with LF and EOI.
inst.read_termination = '\r\n'
inst.write_termination = '\n'

# Query the device with the following message: '\*IDN?'. 
# Which is the standard GPIB message for “what are you?” or – in some cases – “what’s on your display at the moment?”.
# https://pyvisa.readthedocs.io/en/latest/introduction/communication.html
inst.query('*IDN?')

# inst.query('*IDN?')

# TEST: read raw data - success
# inst.write('CURV?')
# data = inst.read_raw()

# TEST: what's on the display at the moment?
# inst.query("*IDN?")



# TEST: acquire waveform from the scope and plot
# values0 = inst.query_ascii_values('CURV?')
# print(values0)

# values1 = inst.query_ascii_values('CURV?', container=numpy.array)
# print(values1)

# values2 = inst.query_ascii_values('CURV?', container=numpy.array, converter='x')
# print(values2)

#plt.plot(values)
#plt.show()