def find_first_index(arr, element, index=0):
    """
    Function to find the first index of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    int: The first index of the element in the array, or -1 if not found.
    """
    if index == len(arr):
        return -1
    if arr[index] == element:
        return index
    return find_first_index(arr, element, index + 1)
