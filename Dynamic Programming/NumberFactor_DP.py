'''
This program demonstrates the implementation of Number factor problem using Dynamic programming
method:

Approach : Top Down with Memoization
'''
def NumberFactor(n, Hash = {0:1, 1:1, 2:2, 3:2}):
    if n in Hash:
        return Hash[n]
    else:
        option1 = NumberFactor(n-1, Hash)
        option2 = NumberFactor(n-3, Hash)
        option3 = NumberFactor(n-4, Hash)
        Hash[n] = option1 + option2 + option3
        return Hash[n]

print(NumberFactor(25))
    