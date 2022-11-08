'''
this program demonstrates the imlementation of Divide and conquer technique for solving 
number of factore problem

problem statement:
    Given a number N, find the number of ways to express N as a sum of {1,3,4}.
'''

def numberOfFactors(N):
    if N in (0,1,2):
        return 1
    elif N == 3:
        return 2
    else:
        sub1 = numberOfFactors(N - 1)
        sub2 = numberOfFactors(N - 3)
        sub3 = numberOfFactors(N - 4)
        return sub1 + sub2 + sub3

print(numberOfFactors(7))