from serial import Serial, SerialException
import threading
import time

class Sender():
    def __init__(self, port="/dev/ttyACM0"):
         self.port = port
    
    def open(self)->None:
        try:
          self.ser = Serial(self.port, baudrate=115200)
        except SerialException as ex:
            print(ex.__cause__)
            time.sleep(60) # sleep for one minute and call again(recursive)
            self.open()
        finally:
            pass

    def close(self)->None:
        self.ser.close()

    def send(self,payload:str)->None:
        '''
         payload example:  '12.5|35.55'
         12.5 is Frequency in Mhz
         35.55 is power in dBm
        '''
        data = payload.encode()
        print('Sending Data:' + payload)
        self.ser.write(data)
        print('Data has been sent now')
        print("*********************\n\n")


def main()->None:
   print("Starting the daemon threads ...")
   sender = Sender()
   threading.Thread(target= sender.send, daemon=False).start()


if __name__ == '__main__':
    main()



