'''
This program demonstrates the implementation of House Robber problem using Dynamic programming
concept:

Approach: Bottom Up with Memoization
'''

def HouseRobber(houses):
    TempTable = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        TempTable[i] = max(TempTable[i+2] + houses[i], TempTable[i+1])
    return TempTable[0]



# simple implementation
# def HouseRobber(houses):
#     temp = 0
#     first = 0
#     second = 0
#     for i in range(len(houses) -1, -1, -1):
#         temp = max(first + houses[i], second)
#         first = second
#         second = temp
#     return temp

houses = [1,12,4,55,39,2,34,2,43,46]
print(HouseRobber(houses))