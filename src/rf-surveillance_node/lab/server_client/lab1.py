import numpy as np

if __name__ == '__main__':
   #frequencies = np.arange(self.start_freq,self.stop_freq, self.step_size)
   frequencies = np.arange(105.5e6, 1700.5e6,100e3,np.float64)
   print(type(frequencies))
   print(frequencies[0])
   print(type(frequencies[0])) # np.float64
   bytesObj = frequencies.tobytes()
   print(f'bytes size {len(bytesObj)}') # bytes size 127600
   print(type(bytesObj))
   frequencies =np.frombuffer(bytesObj,np.float64)
   print(type(frequencies))
   print(frequencies.size) #15950
