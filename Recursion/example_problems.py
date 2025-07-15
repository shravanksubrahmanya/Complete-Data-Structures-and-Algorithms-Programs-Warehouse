import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

def factorial(n):
    '''calculate the factorial of a number n'''
    return n * factorial(n-1) if n > 1 else 1

print(factorial(5))  # Output: 120


'''problem to find 2**n using recursion'''
def power_of_two(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    # first assume that you found the answer  by calling function(n-1)
    small_answer = power_of_two(n-1) # -> Assume: induction hypothesis
    
    # now use the small answer and multiply it with 2 and return
    ans= 2 * small_answer # calculation for just current iteration
    return ans

print(power_of_two(5))  # Output: 32

# program to find number of digits in a number using recursion
def count_digits(n):
    if n >=0 and n <10:
        return 1
    sub_ans = count_digits(n//10) # assume: induction hypothesis, answer for the count of digits will be returned for n // 10
    ans = 1 + sub_ans
    return ans

print(count_digits(12345))  # Output: 5


# fibonacci
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))  # Output: 5


# tail recursion
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    accumulator *= n
    return tail_recursive_factorial(n-1, accumulator)

print(tail_recursive_factorial(5))  # Output: 120