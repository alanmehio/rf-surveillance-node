from threading import Thread
from serial import Serial
from datetime import datetime
import time


class Receiver():
    
    def __init__(self, frequency:float, power:float, device:str):
        self.frequency = frequency/1000
        self.power = power 
        self.devie = device
        print(str(frequency))
        print(str(power))
        print(device)


    def start(self):
        print(f'Frequency(Mhz)\t Power(dBm)\t time\t')
        port = '/dev/' + self.devie
        ser = Serial(port=port, baudrate=115200)
        while True:
            if ser.in_waiting >0:
                msg = ser.read_all()
                message= str(msg.decode()) # 15.55|65.69
                self.display_value(message=message)      
            time.sleep(self.frequency) # 50 ms
    
    def display_value(self, message:str)->None:
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y %H:%M:%S")
        try:
            values:list[str] = message.split("|")
            if float(values[1]) >= self.power:
                print('\a')
                print('\a')
                print('\a')
                print(f'\033[91m{values[0]}\t\t {values[1]}\t\t {date_time}\t\t \033[0m')
            else:
               print(f'\033[92m{values[0]}\t\t {values[1]}\t\t {date_time}\t\t \033[0m') 

            print("\n")
        except IndexError as ex: 
            pass 

       

if __name__ == "__main__":
    receiver = Receiver(50.00, 60.00,"ttyACM0")
    receiver.start()
