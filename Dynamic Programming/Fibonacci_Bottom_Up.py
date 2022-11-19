'''
This program demonstrates the Implementation of fibonacci series using dynamic programming 
concept:

Approach : Bottom up with memoization
'''

# for bottom up we can use python lists for memoization

def Fibonacci(n):
    MemoList = [0,1]
    if n == 0:
        return MemoList[0]
    if n == 1:
        return MemoList[1]
    else:
        for i in range(2,n+1):
            MemoList.append(MemoList[i-1] + MemoList[i - 2])
        return MemoList.pop()

for i in range(20):
    print(Fibonacci(i), end = ' ')