'''Multithreading with threadpool executor'''

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):  
    time.sleep(1)
    return f"Number: {number}"

numbers = [1,2,3,4,5,6,7,8,9,10]

start_time = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    # 3 threads will be created here
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)

finished_time = time.time()
print(f"Time taken: {finished_time - start_time} seconds")