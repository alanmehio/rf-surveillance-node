from rtlsdr import RtlSdr
import numpy as np
import platform
from broker import DataBroker
from scanner import Scanner
from device_manager import DeviceManager
from common.setting import Setting
from common.log_manager import LogManager
from common.util import Util
from rf_sender.css.sender import Sender
import argparse


'''
$ export PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ pwd
 /home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ python3 rfnode setting.json -vvv -ld /home/alan/tmp
'''
def main()-> None:

    parser = argparse.ArgumentParser()
    parser.add_argument("setting", help="path to setting file", type=str,metavar="file")
    parser.add_argument("-ld", "--log_directory", help="store output log in a directory",type=str,metavar="dir")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()

    LogManager().config_logger(args.verbose, args.log_directory)
    Setting.load_setting(args.setting)

    data_broker = DataBroker()

    port:str =''
    if platform.system() == 'Windows':
        port = Setting.rf_sender_port_windows
    else:
        port ='/dev/' + Setting.rf_sender_port

    sender:Sender = Sender(port=port, hold=Setting.rf_sleep_time)
    data_broker.set_rf_sender(sender)

    data_broker.start()

    serial_numbers = DeviceManager.get_device_serial_list()
    frequencies = Util.generate_array(Setting.freq_start, Setting.freq_end, Setting.freq_step, len(serial_numbers))
    print(f'RTL SDR numbers {len(serial_numbers)}')

    scanners = [] # a list of scanner

    for i in (range(len(serial_numbers))):
        print(f'device index {i}')
        sdr = RtlSdr(device_index=i)
        scanner = Scanner(frequencies=frequencies[i],sample_rate=Setting.sample_rate,
                          sample_size=Setting.sample_size, power_threshold=Setting.power_threshold,
                          sdr=sdr)
        scanners.append(scanner)

    print(f'Started number of threads: {len(scanners)}')
    for scanner in scanners:
        scanner.start()

    for thread in scanners:
        thread.join()
        print(f"Thread {thread.name} is finished now")




   # Block until all tasks are done
    print('Before the join for queue ...')
    DataBroker.q.join()
    print('All work completed')


# this is important so that it does not run from pytest
if __name__ == "__main__":
    main()