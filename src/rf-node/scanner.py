# scan module  talk more 
from rtlsdr import RtlSdr
import numpy as np
from threading import Thread 
from broker import DataBroker


from device_manager import DeviceManager





def display_menu():
    print("""
    ##################################
    #                                #
    #      RTL SDR NODE SCANNER      #
    #                                #
    ##################################
          Thread name here 

    """)
    

class Scanner(Thread):
    # The values comes from a Setting class to different range and steps
    def __init__(self, start_freq:str, stop_freq:str, step_size:str, sdr: RtlSdr):
        Thread.__init__(self)
        self.start_freq = int(float(start_freq)*1e6)
        self.stop_freq = int(float(stop_freq)*1e6)
        self.step_size = int(float(step_size)*1e3)
        self.sdr = sdr
        self.sample_rate = 3.2e6 # Hz configured
        self.gain = 'auto'

    def set_sdr(self,sdr:RtlSdr):
        self.sdr = sdr


    def run(self):
        print(f'Starting {self.name} thread ')
        sample_size = 1024*1024 # Alan configure it 
        frequencies = np.arange(self.start_freq,self.stop_freq, self.step_size)
        power_levels = []
        print(f"Scanning from {self.start_freq/1e6} MHz to {self.stop_freq/1e6} MHz...")
        for freq in frequencies:
            self.sdr.center_freq =freq
            samples = self.sdr.read_samples(sample_size)
            spectrum = np.fft.fftshift(np.abs(np.fft.fft(samples))**2)
            power = 10*np.log10(np.mean(spectrum))
            if(power> 55.0): # configure the power to send the sample
                print(f' power is {power}')
                DataBroker.q.put(samples)
            power_levels.append(power)
        
        self.sdr.close()

        threshold = np.mean(power_levels) + np.std(power_levels)
        high_power_indices = np.where(np.array(power_levels) > threshold)[0] # tuple (np.array(),)
        high_power_freqs = frequencies[high_power_indices]/1e6 # numpy array sending array of indices  into a np array
        print("High Power frequencies detected at (MHz):", high_power_freqs)
        print('Sending the result to the queue')
        # Alan we need to send the samlpes also for the analyser to extract information may be if we can 
        # define our threshold to capture the samples 
        DataBroker.q.put(high_power_freqs)



if __name__ == "__main__":
    serial_numbers = DeviceManager.get_device_serial_list()
    print(f' RTL SDR numbers {len(serial_numbers)}')

    scanners = [] # a list of scanner

    for i in (range(len(serial_numbers))):
        # pass the serial number directly
        #print(f'serial number {serial_number}')
        # Find the device index for a given serial number
        #device_index = RtlSdr.get_device_index_by_serial(serial_number)
        print(f'device index {i}')
        sdr = RtlSdr(device_index=i)
        # Alan check for null or if there will be exception etc..
        scanner = Scanner('101.5','102.5','100', sdr)
        #scanner = Scanner('102.1','102.3','100', sdr)
        #thread1.name = 'Scanner one '
        scanners.append(scanner)

    

    for scanner in scanners:
        scanner.start()

    print(f'Started number of threads: {len(scanners)}')
    for thread in scanners:
        print("waiting for the thread " + thread.name + " to finish")
        thread.join()



         
        
