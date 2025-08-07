'''Binary search using recursion'''

def binary_search_recursive(arr, target):
    def helper(left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)
    return helper(0, len(arr) - 1)

# Example usage
li = [1, 2, 2, 2, 3, 5, 6, 8]
target = 3
result = binary_search_recursive(li, target)
print(result)  # Output: 1 (the index of one occurrence of the target)