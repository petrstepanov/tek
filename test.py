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
#    # htt

def handle_event(resource, event, user_handle):
    resource.called = True
    print(f"Handled event {event.event_type} on {resource}")
    
#    # Query '?' tests both reading and writing    
#    instr.write(string)
#    # We need to decode string in Python3: https://stackabuse.com/convert-bytes-to-string-in-python/
#    output = instr.read()
#    print(type(output))
#    # str(output, 'UTF-8')
#    return output

    

# Docs here: https://pyvisa.readthedocs.io/en/latest/index.html
pyvisa.log_to_screen()
print("PyVisa version", pyvisa.__version__)
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

# Open oscilloscope
with rm.open_resource(addr) as instr:

    
    # Configure the instrument
    # https://pyvisa.readthedocs.io/en/latest/introduction/communication.html#getting-the-instrument-configuration-right
    # p.2-5 Programmers manual: 
    # | This oscilloscope does not support ASCII LF only message termination. The
    # | oscilloscope always terminates outgoing messages with LF and EOI.
    instr.read_termination = '\n'   # '\n\r', '\r\n', '\r' not work 
    instr.write_termination = '\n'
    
    # Obtain oscilloscope identification code (manual, p.2-350):
    instr.write('*IDN?')        # 
    scopeCode = instr.read()
    print(scopeCode)
    
    # Tip: instr.query('*IDN?') is same as:
    # instr.write('*IDN?')
    # print(instr.read())
    
    # TEST: read raw data - success
    instr.write('CURV?')
    data = instr.read_raw()
    
    # TEST (FAIL): if oscilloscope is configured to transfer data in ASCII
    # values = instr.query_ascii_values('CURV?')
    # print(values)
    
    # TEST: if oscilloscope is configured to transfer data in ASCII
    # Binary data typ[es list: https://docs.python.org/3/library/struct.html#format-characters
    channels = [1, 2]
    now = datetime.now()    # remember current time
    
    plt.clf()               # configure plot
    plt.grid(True)
    plt.xlabel('Channel')
    plt.ylabel('Amplitude, mV')
    fileName = now.strftime("%Y-%m-%d-%H-%M-%S")
    
    # save CSV file
    values = []
    instr.write('SAVe:WAVEform:FILEFormat SPREADSheet')
    
    for channel in channels:
        # Select source
        instr.write('DATa:SOUrce CH' + str(channel))
        values = instr.query_binary_values('CURV?', datatype='b', is_big_endian=True)
        print(values)
    
        # Construct filename
    
        # Plot valaues
        plt.plot(values)
    
    # TODO: use SAVe:WAVEform instead - it creates header automatically
    instr.write('SAVe:WAVEform:FILEFormat SPREADSheet')
    instr.write('SAVe:WAVEform ALL, "E:/' + fileName + '.csv"')
    
    plt.savefig('/cuanas/Data/' + fileName + '.png')
    # plt.show()
    
    # Start infinite loop
    #i=0
    scope = instr
    while i < 3:
    #instr.write('TRIGger:STATE?')
    #triggerState = instr.read()
    #print(triggerState)
        waiting = 1
        looptime = datetime.now()
        
        # wait here until trigger received, forced trigger occurs or time ends
        while (waiting == 1):
            waiting = int(scope.ask("ACQ:STATE?"))
            #capture the trigger time
            if waiting == 0:
                triggertime = datetime.now()
            if looptime > end_time:
                if scope.query("TRIGGER:STATE?") == 'READY':
                    print("No trigger event for finale capture")
                    break


'''
# PyVisa wait for trigger: https://pyvisa.readthedocs.io/en/latest/introduction/example.html
# ERROR: builtins.AttributeError: 'TCPIPInstrument' object has no attribute 'wait_for_srq'
instr.assert_trigger()
instr.wait_for_srq()
'''

'''
# Trigger event handling: https://pyvisa.readthedocs.io/en/latest/introduction/event_handling.html
# ERROR at instr.install_handler(): builtins.NotImplementedError
instr.called = False

# Type of event we want to be notified about
event_type = pyvisa.constants.EventType.service_request
# Mechanism by which we want to be notified
event_mech = pyvisa.constants.EventMechanism.queue

wrapped = instr.wrap_handler(handle_event)

user_handle = instr.install_handler(event_type, wrapped, 42)
instr.enable_event(event_type, event_mech, None)

# Instrument specific code to enable service request
# (for example on operation complete OPC)
instr.write("*SRE 1")
instr.write("INIT")

while not instr.called:
    sleep(10)

instr.disable_event(event_type, event_mech)
instr.uninstall_handler(event_type, wrapped, user_handle)
'''

rm.close()