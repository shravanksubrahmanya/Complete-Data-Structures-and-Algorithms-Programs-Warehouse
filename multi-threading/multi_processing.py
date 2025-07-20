# processes that runs in parellel
import multiprocessing
import time

def sqare_numbers(n = 5):
    for i in range(n):
        print(f"Square of {i}: {i * i}")
        time.sleep(1)

def cube_numbers(n = 5):
    for i in range(n):
        print(f"Cube of {i}: {i * i * i}")
        time.sleep(1)

if __name__ == "__main__":
    # this is to give entry point for the process where execution of the process starts
    p1 = multiprocessing.Process(target=sqare_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # start the process
    start_time = time.time()
    p1.start()
    p2.start()
    # wait for both processes to finish
    p1.join()
    p2.join()
    finished_time = time.time()
    print(f"Time taken: {finished_time - start_time} seconds")