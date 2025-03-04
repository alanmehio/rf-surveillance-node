from rtlsdr import RtlSdr
from typing import List

class DeviceManager():

    def __init__(self):
        pass

    @staticmethod
    def get_device_serial_list()->list[str]:
        # Get  a list of detected device serial numbers
        # Alan make some check and exception throwing later on
        serial_numbers = RtlSdr.get_device_serial_addresses()
        return serial_numbers
    
    

