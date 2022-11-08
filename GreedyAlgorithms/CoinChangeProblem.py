'''
This program demonstrates the implementation of coin change problem using greedy approach

problem statement:
    You are given coins of diffrent denominations and the total amount of money. Find the 
    minumum number of coins you need to make up the given amount.

    Infinite supply of denominations = {1, 2, 5, 10, 20, 50, 100, 500, 1000}

    Total amount = 2035
'''

def findMinimumCoins(total, denominations):
    denominations.sort()
    numberOfCoins = {}
    totalNumberOfCoins = 0
    count = -1
    while total > 0:
        coinValue = denominations[count]
        if coinValue <= total:
            currentCoins = total//denominations[count]
            numberOfCoins[denominations[count]] = currentCoins
            total %= denominations[count]
            totalNumberOfCoins += currentCoins
        count -= 1
    print("selection of coins : ", numberOfCoins)
    print("Total number of coins: ",  totalNumberOfCoins)

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
amount = 2035
findMinimumCoins(amount, denominations)