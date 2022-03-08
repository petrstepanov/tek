# Install packages on RHEL 8.5 with: pip3.9 install ...
# because nivisa requires python version > ...
# echo 'set path = ($path /usr/local/bin $HOME/bin .)' >> ~/.login
import pyvisa
import matplotlib.pyplot as plt
import numpy
from datetime import datetime
# import usb

def writeFileHeader(inst):
    print('Model,')

#def readDecode(scope, string):
#    # https://pyvisa.readthedocs.io/en/latest/introduction/communication.html
#    # Query '?' tests both reading and writing    
#    scope.write(string)
#    # We need to decode string in Python3: https://stackabuse.com/convert-bytes-to-string-in-python/
#    output = scope.read()
#    print(type(output))
#    # str(output, 'UTF-8')
#    return output

    

# Docs here: https://pyvisa.readthedocs.io/en/latest/index.html
pyvisa.log_to_screen()

# Create Resource Manager

# Default IVI backend (FAILS)
# rm = pyvisa.ResourceManager()

# Py backend (WORKS)
rm=pyvisa.ResourceManager('@py')
print(rm.list_resources())

# Establish a conection with the device
# USB (NOT WORK)
# addr = 'USB0::1689::1110::C013681::0::INSTR'Returns the instrument identification data.

# Ethernet (WORKS): https://github.com/pyvisa/pyvisa-py/issues/261
addr = 'TCPIP::192.168.100.36::INSTR'

scope = rm.open_resource(addr)

# Configure the instrument
# https://pyvisa.readthedocs.io/en/latest/introduction/communication.html#getting-the-instrument-configuration-right
# p.2-5 Programmers manual: 
# | This oscilloscope does not support ASCII LF only message termination. The
# | oscilloscope always terminates outgoing messages with LF and EOI.
scope.read_termination = '\n'   # '\n\r', '\r\n', '\r' not work 
scope.write_termination = '\n'

# Obtain oscilloscope identification code (manual, p.2-350):
scope.write('*IDN?')        # 
scopeCode = scope.read()
print(scopeCode)

# Tip: scope.query('*IDN?') is same as:
# scope.write('*IDN?')
# print(instr.read())

# TEST: read raw data - success
scope.write('CURV?')
data = scope.read_raw()

# TEST (FAIL): if oscilloscope is configured to transfer data in ASCII
# values = scope.query_ascii_values('CURV?')
# print(values)

# TEST: if oscilloscope is configured to transfer data in ASCII
# Binary data typ[es list: https://docs.python.org/3/library/struct.html#format-characters
channels = [1, 2]
now = datetime.now()    # remember current time

plt.clf()               # configure plot
plt.grid(True)
plt.xlabel('Channel')
plt.ylabel('Amplitude, mV')
fileName="/cuanas/Data/" + now.strftime("%Y-%m-%d-%H:%M:%S")

# save CSV file
values = []
scope.write('SAVe:WAVEform:FILEFormat SPREADSheet')

for channel in channels:
    # Select source
    scope.write('DATa:SOUrce CH' + str(channel))
    values = scope.query_binary_values('CURV?', datatype='b', is_big_endian=True)
    print(values)

    # Construct filename

    # Plot valaues
    plt.plot(values)

# TODO: use SAVe:WAVEform instead - it creates header automatically
scope.write('SAVe:WAVEform ALL, "E:/' + fileName + '.csv')

plt.savefig(fileName + '.png')
# plt.show()

# Start infinite loop
i=0
while i < 1:
    # scope.assert_trigger()
    # scope.waitait_for_srq()    
    scope.write('TRIGger:STATE?')
    triggerState = scope.read()
    print(triggerState)

rm.close()