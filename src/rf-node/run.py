""" The command line interface (CLI) parser """
from rtlsdr import RtlSdr
import numpy as np
from threading import Thread
from broker import DataBroker
from scanner import Scanner
from device_manager import DeviceManager
from common.setting import Setting
from common.log_manager import LogManager
from common.util import Util
import argparse


'''
python3  src/rf-node/cli.py ../setting.json -vvv -ld /home/alan/tmp
'''
def run()-> None:

    parser = argparse.ArgumentParser()
    parser.add_argument("setting", help="path to setting file", type="str",metavar="file")
    parser.add_argument("-ld", "--log_directory", help="store output log in a directory",type="str",metavar="dir")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    
    LogManager().config_logger(args.verbose, args.log_directory)
    Setting.load_setting(args.setting)

    data_broker = DataBroker()
    data_broker.start()
    
    serial_numbers = DeviceManager.get_device_serial_list()
    frequencies = Util.generate_array(Setting.freq_start, Setting.freq_end, Setting.freq_step, len(serial_numbers))
    print(f' RTL SDR numbers {len(serial_numbers)}')

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
        print("waiting for the thread " + thread.name + " to finish")
        thread.join()



   
   # Block until all tasks are done
    print('Before the join for queue ...')
    DataBroker.q.join()
    print('All work completed')


# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    run()