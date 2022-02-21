# Import PyVISA library
import pyvisa
pyvisa.log_to_screen()

# Create Resource Manager object with default IVI backend (no arguments)
rm = pyvisa.ResourceManager()

# List available resources
# 2022-02-21 17:16:30,623 - pyvisa - DEBUG - viFindRsrc(4097, '?*::INSTR', '<ViObject object at 0x7f1c4f78db40>', 'c_uint(0)', <ctypes.c_char_Array_256 object at 0x7f1c4f6e8d40>) -> -1073807343
# ()
print(rm.list_resources())


#rm.list_resources()
#('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')

#inst = rm.open_resource('GPIB0::12::INSTR')

#print(inst.query("*IDN?"))
