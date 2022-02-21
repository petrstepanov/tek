# Import PyVISA library
import pyvisa
import usb

# Docs here: https://pyvisa.readthedocs.io/en/latest/index.html
pyvisa.log_to_screen()

# Create Resource Manager object with default IVI backend (no arguments)
rm = pyvisa.ResourceManager()
rm.list_resources()
print(rm.list_resources('?*'))

# Create Resource Manager with Py backend
rmpy=pyvisa.ResourceManager('@py')
rmpy.list_resources()
print(rmpy.list_resources('?*'))

# Issue: Found a device whose serial number cannot be read
# Solution: https://www.google.com/search?client=firefox-b-1-e&q=pyvisa+Found+a+device+whose+serial+number+cannot+be+read