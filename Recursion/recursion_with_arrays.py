'''Write a program to check if array is sorted using recursion'''

arr = [1, 2, 3, 4, 5]
a2rr = [1, 3, 2, 4, 5]  # Example of unsorted array

# head recursion
def is_sorted(arr, index=0):
    n = len(arr)
    if index == n-1:
        return True
    if arr[index] <= arr[index+1]:
        return is_sorted(arr, index+1)
    else:
        return False

print(is_sorted(arr))  # Output: True
print(is_sorted(a2rr))  # Output: False

# Tail recursion
def is_sorted_tail(arr, index=0):
    n = len(arr)
    if index == n-1:
        return True
    elif arr[index] > arr[index+1]:
        return False
    else:
        return is_sorted_tail(arr, index+1)

print(is_sorted_tail(arr))  # Output: True
print(is_sorted_tail(a2rr))  # Output: False