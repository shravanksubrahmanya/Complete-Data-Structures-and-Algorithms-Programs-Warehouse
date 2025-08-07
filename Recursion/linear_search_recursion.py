'''Searching using recursion'''

def linear_search_recursive(arr, target):
    def helper(index = 0):
        if index == len(arr):
            return -1
        elif arr[index] == target:
            return index
        return helper(index + 1)
    
    return helper()

def alternate_linear_search_recursive(arr, target):
    def helper(index = 0):
        if index == len(arr):
            return False
        
        ansFromRecursion = helper(index + 1)
        
        if ansFromRecursion:
            return True
        
        return arr[index] == target
    
    return helper()

li = [2, 5, 2, 8, 2, 1, 3, 6, 2]
target = 1
result = linear_search_recursive(li, target)
alternate_result = alternate_linear_search_recursive(li, target)
print(result)  # Output: 0 (the first occurrence of the target)
print(alternate_result)  # Output: True (the target exists in the list)