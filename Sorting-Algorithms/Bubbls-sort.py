'''
This program demonstratees the sorting of an array using Bubble sort algorithm
'''

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)


array = [43,98,1,42,0,32,73,67,23,32,65,72,11,19,18]
bubbleSort(array)


