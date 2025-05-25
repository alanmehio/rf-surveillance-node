from threading import Thread
from serial import Serial
from datetime import datetime
import time


#class Receiver(Thread):
class Receiver():
    def __init__(self, port:str):
        #Thread.__init__(self)
        self.port = port


    def start(self):
        print(f'Frequency(Mhz)\t Power(dBm)\t time\t')
        #try:
        ser = Serial(port=self.port, baudrate=115200)
        while True:
            # color 
            # see https://vascosim.medium.com/how-to-print-colored-text-in-python-52f6244e2e30
            # see https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
            # see https://sentry.io/answers/print-colored-text-to-terminal-with-python/
            # Print text in red
           #print(ser.in_waiting )
            if ser.in_waiting >0:
                msg = ser.read_all()
                message= str(msg.decode()) # 15.55|65.69
                #print(f'Received payload:{message}')
                now = datetime.now()
                date_time = now.strftime("%m-%d-%Y %H:%M:%S")
                values:list[str] = message.split("|")
                #print(len(values))
                print(f'\033[31m{values[0]}\t\t {values[1]}\t\t {date_time}\t\t \033[0m')
                print("\n")
            time.sleep(0.1) 
        #except BaseException as ex: # catch all exception 
            #print(ex.__cause__)
            #time.sleep(60) # wait 1 minutes
            #pass


if __name__ == "__main__":
    receiver = Receiver("ttyACM0")
    receiver.start()
