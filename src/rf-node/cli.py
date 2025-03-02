""" The command line interface (CLI) parser """
from rtlsdr import RtlSdr
import numpy as np
from threading import Thread
from broker import DataBroker
from scanner import Scanner
from device_manager import DeviceManager
from conf.setting import Setting
from conf.log_manager import LogManager



def main()-> None:
    data_broker = DataBroker()
    data_broker.start()


    serial_numbers = DeviceManager.get_device_serial_list()
    print(f' RTL SDR numbers {len(serial_numbers)}')

    scanners = [] # a list of scanner

    for i in (range(len(serial_numbers))):
        print(f'device index {i}')
        sdr = RtlSdr(device_index=i)
        # Alan check for null or if there will be exception etc..
        scanner = Scanner('101.5','105.5','100', sdr)
        scanners.append(scanner)

    for scanner in scanners:
        scanner.start()

    print(f'Started number of threads: {len(scanners)}')
    for thread in scanners:
        print("waiting for the thread " + thread.name + " to finish")
        thread.join()



   
   # Block until all tasks are done
    print('Before the join for queue ...')
    DataBroker.q.join()
    print('All work completed')


# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    main()