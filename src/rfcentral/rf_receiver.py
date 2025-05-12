from threading import Thread
import time 


class Receiver(Thread):

    def __init__(self):
        Thread.__init__(self)


    def run(self):
        print(f'Frequency(Mhz)\t Power(dBm)\t time\t')
        while True:
            # color 
            # see https://vascosim.medium.com/how-to-print-colored-text-in-python-52f6244e2e30
            # see https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
            # see https://sentry.io/answers/print-colored-text-to-terminal-with-python/
            # Print text in red
             print(f'\033[31m13.55\t\t 50.66\t\t 2025-05-05 13:13:45\t\t \033[0m')
             
             time.sleep(10)
    




