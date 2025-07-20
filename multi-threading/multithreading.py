import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(2)

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(2)

# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()   
# start the threads
t1.start()
t2.start()

# wait for both threads to finish
t1.join() # once the execution completes both of these threads will join back to the main thread
t2.join()
finished = time.time()
print(f"Time taken: {finished - t} seconds")