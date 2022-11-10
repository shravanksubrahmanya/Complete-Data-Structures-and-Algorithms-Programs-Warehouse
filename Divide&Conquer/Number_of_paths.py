'''
This program demonstrates the problem : "Number of ways to reach the last cell with given cost"
using divide and conquer approach
'''

def NumberOfPaths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[row][col] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return NumberOfPaths(twoDArray,row, col - 1, cost - twoDArray[row][col])
    elif col == 0:
        return NumberOfPaths(twoDArray, row - 1, col, cost - twoDArray[row][col])
    else:
        option1 = NumberOfPaths(twoDArray, row - 1, col, cost - twoDArray[row][col])
        option2 = NumberOfPaths(twoDArray, row, col - 1, cost - twoDArray[row][col])
        return option1 + option2

twoDarray = [
    [1,4,2,5,3],
    [7,8,2,4,2],
    [8,5,2,5,9],
    [2,4,3,7,9],
    [7,4,6,2,4]
    ]
print(NumberOfPaths(twoDarray, 4,4, 35))