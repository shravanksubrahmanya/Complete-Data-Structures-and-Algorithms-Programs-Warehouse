'''
This program demonstrates the zero knapsack problem using divide and conquer approach

problem statement:
    Given weights and profits of n diffrent items, find the maximum profit can be achieved
    wihin given capacity C, items can not be broken

Approach: Bottom Up with Memoization
'''

class Items:
    # since this is a divide and conquer approach there is no necessity to store the ratio 
    # of value and weight
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def zeroKnapSack(itemlist, capacity, currentIndex = 0, itemDict = {}):
    if currentIndex >= len(itemlist) or capacity<=0:
        return 0
    dictKey = str(currentIndex) + str(capacity)
    currentWeight = itemlist[currentIndex].weight
    if currentWeight <= capacity:
        if dictKey not in itemDict:
            selectFirst = itemlist[currentIndex].value + zeroKnapSack(itemlist, capacity - currentWeight, currentIndex + 1, itemDict)
            skipFirst = zeroKnapSack(itemlist, capacity, currentIndex + 1, itemDict)
            itemDict[dictKey] = max(selectFirst, skipFirst)
        return itemDict[dictKey]
    return 0

mango = Items(2,31)
apple = Items(1,26)
orrange = Items(2,17)
banana = Items(5,72)

itemlist = [mango, apple, orrange, banana]
print(zeroKnapSack(itemlist, 7))