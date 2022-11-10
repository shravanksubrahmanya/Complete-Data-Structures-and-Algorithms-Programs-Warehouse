'''
This program demonstrates the zero knapsack problem using divide and conquer approach

problem statement:
    Given weights and profits of n diffrent items, find the maximum profit can be achieved
    wihin given capacity C, items can not be broken
'''

class Items:
    # since this is a divide and conquer approach there is no necessity to store the ratio 
    # of value and weight
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def zeroKnapSack(itemlist, capacity, currentIndex = 0):
    if capacity <= 0 or currentIndex< 0 or currentIndex >= len(itemlist):
        return 0
    currentweight = itemlist[currentIndex].weight
    if currentweight <= capacity:
        profit1 = itemlist[currentIndex].value + zeroKnapSack(itemlist, capacity-currentweight, currentIndex + 1)
        profit2 = zeroKnapSack(itemlist, capacity, currentIndex + 1)
        return max(profit1, profit2)
    return 0

mango = Items(2,31)
apple = Items(1,26)
orrange = Items(2,17)
banana = Items(5,72)

itemlist = [mango, apple, orrange, banana]
print(zeroKnapSack(itemlist, 7))

