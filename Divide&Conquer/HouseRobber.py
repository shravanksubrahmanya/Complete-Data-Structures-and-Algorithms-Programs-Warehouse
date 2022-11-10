'''
This program demonstrates the house robber problem using divide and conquer approach

problem statement:
    if there are n houses, each house is associated with a value. A robber wants to rob the 
    houses in the street based on following condition:
        1. Given N number of houses along the street some amount of money
        2. Adjascent houses can't be stolen as there is a security system connected between 
        two houses
        3. Find the maximum amount that can be stolen
'''

def HouseRobber(houses, currenthouse = 0):
    if currenthouse >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currenthouse] + HouseRobber(houses, currenthouse + 2)
        skipFirstHouse = HouseRobber(houses, currenthouse + 1)
        return max(stealFirstHouse, skipFirstHouse)

houses = [1,6,23,30,7,9,7]
print(HouseRobber(houses))