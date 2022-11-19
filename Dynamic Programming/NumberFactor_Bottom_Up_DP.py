'''
This program demonstrates the implementation of Number factor problem using Dynamic programming
method:

Approach : Bottom up with Memoization
'''

def NumberFactor(n):
    table = [1,1,1,2]
    for i in range(4, n+1):
        table.append(table[i-1] + table[i-3] + table[i-4])
    return table[n]

print(NumberFactor(1000))
    