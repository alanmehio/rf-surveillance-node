
'''
Linux:
=====
$ export PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ pwd
 /home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ python rfcentral -p 65.55 -d ttyACM0

Windows:
=======
set PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance/src
echo %PYTHONPATH%
python rfcentral  -p 65.55 -d COM4
Note: Check the devicemanager from control panel for the port name
'''
import platform
from argparse import ArgumentParser, Namespace
from .receiver import Receiver
from .displayer import ConsoleOutput
from .broker import DataBroker

def get_cli_value()->tuple[float,float,str]:
   pass

def main()-> None:
     """
    This is the main function that executes the program.
    This function uses argparse to handle input from the command line.

    Command-line arguments
    ----------------------
    -p : float
        energy warning level; default to 50 dBm
    -d : str
        device name default to 'ttyACM0'

    Examples:
        >>> rfcentral -p 65.55 -d ttyACM0
    """
     parser = ArgumentParser(prog="rfcentral", usage="rfcentral -p 65.55 -d ttyACM0",description="RF Central Command Line Interface")


     parser.add_argument(
        '-p',
        help='frequency engergy power level; if exceeded will give beep as warning',
        type=float,
        nargs='?',
        default=50.00,
        metavar='power'
     )
     parser.add_argument(
        '-d',
        help= 'device name  or RF device receiver name',
        type= str,
        default = 'ttyACM0',
        nargs='?',
        metavar = 'device'

     )

     args : Namespace = parser.parse_args()
     power:float = args.p
     device:str = args.d

     port:str
     if platform.system() == 'Windows':
         port = device
     else:
         port ='/dev/' + device

     out = ConsoleOutput(power)
     data_broker = DataBroker()
     data_broker.start()
     receiver = Receiver(out, port=port)
     receiver.start() # execute in a separate thread


# this is important so that it does not run from pytest
if __name__ == "__main__":
    main()

