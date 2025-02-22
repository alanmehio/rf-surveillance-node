from rtlsdr import  RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.04e6 # Hz
sdr.center_freq = 105.5e6
sdr.freq_correction = 1 # PPM
sdr.gain = 'auto'
arr = sdr.read_samples(512)
print(type(arr))
print (arr.size)
print(arr)


