'''
This program demonstrates the implementation of House Robber problem using Dynamic programming
concept:

Approach: Top Down with Memoization
'''

def HouseRobber(houses, currentHouse, houseDict):
    if currentHouse >= len(houses):
        return 0
    else:
        if houses[currentHouse] not in houseDict:
            stealFirstHouse = houses[currentHouse] + HouseRobber(houses, currentHouse + 2, houseDict)
            skipFirstHouse = HouseRobber(houses, currentHouse + 1, houseDict)
            houseDict[currentHouse] = max(stealFirstHouse, skipFirstHouse)
        return houseDict[currentHouse]

houses = [1,12,4,55,39,2,34,2,43,46]
print(HouseRobber(houses, 0, {}))