'''
This Algorithm Demonstrates the sorting of an array using Merge sort algorithm
'''
def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l+i]
    
    for j in range(0, n2):
        R[j] = customList[m+1+j]
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

# def mergeSort(customList, l, r):
#     if l < r:
#         m = (l+(r-1))//2
#         mergeSort(customList, l, m)
#         mergeSort(customList, m+1, r)
#         merge(customList, l, m, r)
#     return customList

# def Merge(array, left, middle, right):
#     n1 = middle - left + 1
#     n2 = right - middle
#     L = [0] * (n1)
#     R = [0] * (n2)

#     for i in range(0, n1):
#         L[i] = array[left+i]
    
#     for j in range(0, n2):
#         R[j] = array[middle+1+j]

#     i = 0
#     j = 0
#     k = left
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             array[k] =  L[i]
#             i += 1
#         else:
#             array[k] = R[j]
#             j += 1
#         k += 1
    
#     while i< n1:
#         array[k] = L[i]
#         i += 1
#         k += 1

#     while j < n2:
#         array[k] = R[i]
#         j += 1
#         k += 1

def MergeSort(array, left, right):
    if left < right:
        midIndex = (left + right - 1) // 2
        MergeSort(array, left, midIndex)
        MergeSort(array,midIndex+1, right)
        merge(array,left, midIndex, right)
    else:
        return array

array = [43,98,1,42,0,32,73,67,23,32,65,72,11,19,18]
print(array)
print(MergeSort(array,0,len(array)-1))
print(array)