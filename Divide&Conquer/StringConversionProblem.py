'''
This program demonstrates the string conversion problem using divide and conquer approach.

problem statement:
    there are two given strings S1 and S2, convert S2 to S1 using delete, insert or replace 
    operations and return the minimum number of operations needs to be performed to convert 
    the string.
'''

def findMinOperations(s1,s2,index1 = 0, index2 = 0):
    if index1 == len(s1):
        # if one string is empty then number of insert operations needs to be ferformed is
        # equal to elements left in the second string
        return len(s2) - index2 
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        # if the current index elements are same then we are moving next position
        return findMinOperations(s1,s2, index1 + 1, index2 + 1)
    else:
        # count the number of operations reuired if we perform insert, delete, and replace
        deleteop = 1 + findMinOperations(s1, s2, index1, index2 + 1)
        insertop = 1 + findMinOperations(s1, s2, index1 +1, index2)
        replaceop = 1 + findMinOperations(s1, s2, index1 + 1, index2 + 1)
        # return minimum number of operations
        return min(deleteop, insertop, replaceop)

print(findMinOperations("table", "tgblce"))


