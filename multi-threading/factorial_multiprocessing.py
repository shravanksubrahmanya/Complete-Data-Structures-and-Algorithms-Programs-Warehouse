import multiprocessing
import multiprocessing.pool
import time
import sys
import math

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of a given number
def compute_factorial(n):
    print(f"Computing factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000]  # large numbers for factorial computation
    start_time = time.time()
    # create a pool or worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)
    
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
        