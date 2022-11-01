'''
This program demonstrates the sorting of an array using bucket sort algorithm
here insertion sort algorithm is used by bucket sort algorithm
# Note: Observe how element 0 is sorted by changing index of the buckets
# note: start the calculation from bucket 1 instead of bucket 0, which makes calculation
  easier
'''
import math

def insertionSort(array):
    for i in range(1,len(array)):
        currentElement = array[i]
        j = i - 1
        while j >= 0 and currentElement < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = currentElement
    return array

# the bucket sort uses insertion sort algorithm to sort the elemenets of tha bucket
def bucketSort(array):
    NoOfBuckets = round(math.sqrt(len(array)))
    maxVal = max(array)
    buckets = []

    # creating number of Buckets
    buckets.extend([[] for x in range(NoOfBuckets+1)])

    for i in array:
        BucketIndex = math.ceil(i * NoOfBuckets / maxVal)
        buckets[BucketIndex].append(i)
    
    array = []
    for subarr in buckets:
        array.extend(insertionSort(subarr))
    
    print(array)


array = [43,98,1,42,0,32,73,67,23,32,65,72,11,19,18]
bucketSort(array)