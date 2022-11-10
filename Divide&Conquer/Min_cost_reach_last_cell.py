'''
This program demonstrates the minimum cost to reach the last cell using divide and 
conquer approach
'''
import numpy as np

def minCostRLC(twoDarray, row, column):
    if row < 0 or column < 0:
        return float('inf')
    elif row == 0 and column == 0:
        return twoDarray[row][column]
    else:
        option1 = minCostRLC(twoDarray, row, column - 1) # go up
        option2 = minCostRLC(twoDarray, row - 1, column) # go left
        return twoDarray[row][column] + min(option1, option2)

twoDarray = np.random.randint(20, size=25).reshape(5,5)
print(minCostRLC(twoDarray, 4,4))