'''
This program demonstrates sorting of an array based on heap sort algorithm
'''

def Heapify(array, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[l] <array[smallest]:
        smallest = l
    
    if r < n and array[r] < array[smallest]:
        smallest = r

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        Heapify(array, n, smallest)

def HeapSort(array):
    n = len(array)
    for i in range(int(n/2)-1, -1, -1):
        Heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        Heapify(array, i, 0)

    array.reverse()

array = [43,98,1,42,0,32,73,67,23,32,65,72,11,19,18]
HeapSort(array)
print(array)
