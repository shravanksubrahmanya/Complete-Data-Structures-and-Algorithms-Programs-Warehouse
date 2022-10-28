'''
The below program demonstrates merging of two sorted arrays

test case 1:

a1 = [1,2,6,8,78]
a2 = [3,7,45,56]
'''

# each element should be compared
# left array element should be compared with right array element
# if left array element is greater or equal to it, add it to sorted array, and move to next element of left array
# if right array element is greater add it to sorted array, move to next element of right array
# add all the remaining element of array which is not exhausted.


'''
checks:
1. array can contain non integer, alphanumeric, special characters
2. array can contain zero elements
'''
def MergeSortedArray(array1, array2):
    i = 0
    j = 0
    MergedArray = []
    while(i < len(array1)) and (j < len(array2)):
        if array1[i] <= array2[j]:
            MergedArray.append(array1[i])
            i += 1
        else:
            MergedArray.append(array2[j])
            j += 1
    
    if i < len(array1):
        MergedArray.extend(array1[i:])
    if j < len(array2):
        MergedArray.extend(array2[j:])
    
    return MergedArray

a1 = [1,2,6,8,78]
a2 = [3,7,45,56]
print(MergeSortedArray(a1,a2))