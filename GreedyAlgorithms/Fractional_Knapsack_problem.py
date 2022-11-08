'''
This program demonstrates the fractional knapsack problem
'''

# item class
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = self.value / self.weight

def knapsack(items, capacity):
    items.sort(key = lambda x: x.ratio, reverse = True)
    takenItems = {}
    totalValue = 0

    for item in items:
        if item.weight > capacity:
            usableWeightRatio = capacity / item.weight
            totalValue += item.value * usableWeightRatio
            capacity = 0
            takenItems[item.weight] = item.value * usableWeightRatio
            break
        else:
            totalValue += item.value
            capacity -= item.weight
            takenItems[item.weight] = item.value
    print(totalValue)
    print(takenItems)

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10, 50)
item4 = Item(15,45)
itemList = [item1,item2,item3,item4]

knapsack(itemList, 50)