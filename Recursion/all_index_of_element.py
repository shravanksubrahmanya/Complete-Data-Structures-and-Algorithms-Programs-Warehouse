'''
Write a program to find all index of a given element.
results have to be as below

1. Print indexes
2. Update the answer in list povided
3. update indices in global list
4. Return answer as a new list
'''

def printAllIndicesOfElement(li, e, index = 0):
    if index == len(li):
        return
    elif li[index] == e:
        print(index)
    return printAllIndicesOfElement(li, e, index + 1) 

def returnAllIndicesInList(li, e, index = 0):
    if index == len(li):
        return []
    
    smalllist = returnAllIndicesInList(li, e, index + 1)
    
    if li[index] == e:
        smalllist.insert(0, index)
    return smalllist


li = [2,5,2,8,2,1,3,6,2]
ele = 2

printAllIndicesOfElement(li, ele)

res = returnAllIndicesInList(li, ele)
print(res)