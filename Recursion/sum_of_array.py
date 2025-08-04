'''this code demonstrates how to use recursion to find the sum of an array'''

# head recursion
def sum_of_array(arr):
    if len(arr) == 0:
        return 0
    ans = sum_of_array(arr[1:])
    return arr[0] + ans

# Example usage
arr = [1, 2, 3, 4, 5]
print("Head Recursion: Sum of array =", sum_of_array(arr))  # Output: 15

# tail recursion
def sum_of_array_tail(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_of_array_tail(arr[1:])

# Example usage
print("Tail Recursion: Sum of array =", sum_of_array_tail(arr))  # Output: 15

# Alternate approach using tail recursion
def sum_of_array_alternate(arr, index=0, accumulator=0):
    if index == len(arr):
        return accumulator
    accumulator += arr[index]
    return sum_of_array_alternate(arr, index + 1, accumulator)

# Example usage

print("Alternate Approach tail Recursion: Sum of array =", sum_of_array_alternate(arr))