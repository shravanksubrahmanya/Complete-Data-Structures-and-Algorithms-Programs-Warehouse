'''multiprocessing with ProcessPoolExecutor example'''

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f"Square of {number}: {number * number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        # 3 processes will be created here
        result = executor.map(square_numbers, numbers)

    for res in result:
        print(res)

    finished_time = time.time()

    print(f"Time taken: {finished_time - start_time} seconds")