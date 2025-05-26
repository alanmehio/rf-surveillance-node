
'''
$ export PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ pwd 
 /home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ python rfcentral -f 50 -e 65.55 -p ttyACM0
'''
from argparse import ArgumentParser, Namespace  
from rf_receiver.css.receiver import Receiver

def get_cli_value()->tuple[float,float,str]:
   pass

def main()-> None:
     """
    This is the main function that executes the program.
    This function uses argparse to handle input from the command line.
    
    Command-line arguments
    ----------------------
    -f : float
       frequency of pulling in milli seconds (ms)
       default to 50 ms if not given.
    -p : float
        energy warning level; default to 50 dBm
    -d : str
        device name default to 'ttyACM0'

    Examples:
        >>> rfcentral -f 50 -p 65.55 -d ttyACM0
    """
     parser = ArgumentParser(prog="rfcentral", usage="rfcentral -f 50 -p 65.55 -d ttyACM0",description="RF Central Command Line Interface")

     parser.add_argument(
        '-f',
        help= 'pulling frequency for the RF receiver',
        type= float,
        default=50.00,
        nargs='?',
        metavar='frequency'
     )
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
     frequency:float = args.f
     power:float = args.p
     device:str = args.d
     receiver = Receiver(frequency=frequency, power=power, device=device) 
     receiver.start()
   

# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    main()

