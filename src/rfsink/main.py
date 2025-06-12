import sys
from PySide6 import QtWidgets
from rfsink.windows.main_window import MainWindow
import argparse
from rfsink import __version__

def main()-> None:

   parser = argparse.ArgumentParser()
   parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
   args = parser.parse_args()

   app = QtWidgets.QApplication()
   
   widget = MainWindow()
   widget.show()

   sys.exit(app.exec()) 

# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    main()