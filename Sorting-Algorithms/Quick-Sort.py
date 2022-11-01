'''
This program demonstrates the sorting of an array using QUICK SORT algorithm
'''

from time import sleep

'''
# method one 

def partition(array, left, right):
    # find pivot element 
    # move lesser value elements to the left of pivot element 
    # move higher value elements to the right of pivot element
    # return partition index

    pivot = array[right]
    i = left
    j = right - 1
    
    while i < j:
        while pivot > array[i]:
            i += 1
        while pivot < array[j]:
            j -= 1
        array[i],array[j] = array[j],array[i]
        # print(array)
        # sleep(1)
    # swap back
    array[i],array[j] = array[j],array[i]
    # swap pivot with i
    array[i], array[right] = pivot, array[i]
    return i
'''

# method two

def partition(array, low, high):
    i = low -1
    pivot = array[high]

    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def QuickSort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        QuickSort(array, left, p-1)
        QuickSort(array, p + 1, right)

array = [43,98,1,42,0,32,73,67,23,32,65,72,11,19,18]
QuickSort(array, 0, len(array) - 1)
print(array)
    