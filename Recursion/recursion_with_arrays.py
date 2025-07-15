'''Write a program to check if array is sorted using recursion'''

arr = [1, 2, 3, 4, 5]
a2rr = [1, 3, 2, 4, 5]  # Example of unsorted array

print("Head recurstion")
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

print("Tail Recursion")
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


'''Alternate approach to check if array is sorted using recursion'''
print("Alternate Approach head recursion")
# head recursion
def is_sorted_alternate(arr):
    if len(arr) <= 1:
        return True
    ans = is_sorted_alternate(arr[1:])
    if arr[0] <= arr[1]:
        return ans
    else:
        return False

print(is_sorted_alternate(arr))  # Output: True
print(is_sorted_alternate(a2rr))  # Output: False

print("Alternate Approach Tail recursion")
def is_sorted_alternate_tail(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted_alternate_tail(arr[1:])

print(is_sorted_alternate_tail(arr))  # Output: True
print(is_sorted_alternate_tail(a2rr))  # Output: False