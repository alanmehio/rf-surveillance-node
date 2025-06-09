#
# 


APP_NAME = 'RF Surveilance '

F_MIN = 0 # fix alan
F_MAX = 9999 #fix alan
GAIN = 0
SAMPLE_RATE = 2e6 # fix alan
BANDWIDTH = 500e3

LOCATION_PORT = 7786

MODE = ["Single", 0,
        "Continuous", 1,
        "Maximum", 2]

NFFT = [16,
        32,
        64,
        128,
        256,
        512,
        1024,
        2048,
        4096,
        8192,
        16384,
        32768]





if __name__ == '__main__':
    print('Please run ?????.py')
    exit(1)
