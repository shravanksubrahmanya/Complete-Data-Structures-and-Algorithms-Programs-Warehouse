'''
This program demonstrates the memoization concept of dynamic programming using fibonacci
sequence
'''

fibHash = {0: 0, 1: 1}

def fibonacci(n):
    if n in fibHash:
        return fibHash[n]
    else:
        fibHash[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibHash[n]

for i in range(1000):
    print(fibonacci(i), end = " ")