'''
This program demonstrates the sorting of an array based on insertion sort algorithm
'''

from array import array


def insertionSort(array):
    for i in range(len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    print(array)

array = [43,98,1,42,0,32,73,67,23,32,65,72,11,19,18]
insertionSort(array)