
'''
$ export PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance-center/src
$ pwd 
 /home/alan/workspace-python/RTL-SDR/rf-surveillance-center/src
$ python3 rfserver ????
'''
def main()-> None:
   print("main..")

# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    main()