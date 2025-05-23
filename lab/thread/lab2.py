import threading
import queue

# readhttps://docs.python.org/3/library/queue.html 
q= queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished{item}')
        q.task_done()


# Turn on the work thread
threading.Thread(target= worker, daemon=True).start()


# Send thirty task request to the worker 
for item in range(30):
    q.put(item)
    

# Block until all tasks are done
q.join()
print('All work completed')
