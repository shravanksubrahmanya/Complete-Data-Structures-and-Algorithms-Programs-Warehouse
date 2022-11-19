'''
This program demonstrates the memoization concept of dynamic programming using fibonacci
sequence
approach: Top down with Memoization
'''



def fibonacci(n, fibHash):
    if n in fibHash:
        return fibHash[n]
    else:
        fibHash[n] = fibonacci(n-1, fibHash) + fibonacci(n-2, fibHash)
        return fibHash[n]

fibHash = {0:0, 1:1}
for i in range(1000):
    print(fibonacci(i, fibHash), end = " ")