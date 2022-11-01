'''
This program demonstrates the sorting of algorithm using selection sort
'''

from tkinter import SE


def SelectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    print(array)


array = [43,98,1,42,0,32,73,67,23,32,65,72,11,19,18]
SelectionSort(array)