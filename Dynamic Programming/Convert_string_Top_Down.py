'''
This program demonstrates the implementation of String conversion problem using Dynamic
programming approach:

Approach: Top down with memoization
'''

def findMinOperations(s1, s2, index1, index2, tempDict = {}):
    if index1 == len(s1):
        return len(s2) - index2
    elif index2 == len(s2):
        return len(s1) - index1
    elif s1[index1] == s2[index2]:
        return findMinOperations(s1, s2, index1 + 1, index2 + 1, tempDict)
    else:
        dictKey = s1[index1] + s2[index2]
        if dictKey not in tempDict:
            deleteop = 1 + findMinOperations(s1, s2, index1, index2 + 1, tempDict)
            insertop = 1 + findMinOperations(s1, s2, index1 + 1, index2, tempDict)
            replaceop = 1 + findMinOperations(s1, s2, index1 + 1, index2 + 1, tempDict)
            tempDict[dictKey] = min(deleteop, insertop, replaceop)
        return tempDict[dictKey]

print(findMinOperations("leetcode", 'leotcoeed', 0, 0))