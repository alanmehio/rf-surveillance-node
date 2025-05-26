'''
$ export PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ pwd 
 /home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ python rfsink ???
'''
def main()-> None:
   print("main..")

# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    main()