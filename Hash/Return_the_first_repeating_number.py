'''
The below program demonstrates the given problem:
Given an array A, Find the first repeating number and return it,
if there are no repeating numbers return None

test case 1:
A = [2,5,1,2,3,5,1,2,4] // should return 2

test case 2:
A = [2,1,1,2,3,5,1,2,4] // should return 1

test case 3:
A = [2,3,4,5] // should return None
'''

'''
possible solutions:
1. brute Force: use two arrays to traverse (o(n^2))
     * first loop starts from i and second loop starts from j = i + 1
     * loop through all elements,
        * if the element found add both i and j indexes to storage
     * after finishing loop find the pair in new list such that diffrence between i and j
        is minimum

2. brute force: i.e use separate list, store the data in that list
 as we are traversing through current list. if the new element exists in newly created list
 return the number( o(n^2) if we have to traverse through two lists)

3. Use hash tables: why? fetching a  particular value most of the times takes o(1) time complexity
'''

# method 3
# def First_repeating_no(array):
    # if len(set(array)) == len(array):
#         return False
#     HashMap = {}                # instead of dictionary we can use list as well.
#     for i,item in enumerate(array):
#         if item in HashMap:
#             return item
#         HashMap[item] = i
#     return False

# using loops

def First_repeating_no(array):
    # first create two loops to iterate through
    oldi = -1
    curi = -1
    oldj = len(array)
    curj = len(array)
    i = 0

    while True:
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                curi = i
                curj = j
            if (curj - curi) < (oldj - oldi):
                oldi = curi
                oldj = curj
                break
        if i == curj:
            break
        i += 1

    if oldi == -1:
        return None
    return array[oldi]

A = [2,5,1,2,3,5,1,2,4]
print(First_repeating_no(A))