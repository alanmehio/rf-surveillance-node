from rtlsdr import RtlSdr

# Get a list of detected device serial numbers(str)
serial_numbers = RtlSdr.get_device_serial_addresses()
for serial_number in serial_numbers:
     print(serial_number)
     print(type(serial_number))
     # Find the device index for a given serial number
     device_index = RtlSdr.get_device_index_by_serial(serial_number)
     sdr = RtlSdr(device_index)
     print(sdr.fc)
