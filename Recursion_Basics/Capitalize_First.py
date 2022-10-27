# this program capitalizes first letter of each string in an array
# this program uses recursive approach

def capitalizeFirst(arr):
    assert len(arr) > 0, 'Invalid length of arguments'
    # capitalize the first string
    arr[0] = arr[0].capitalize()
    if(len(arr) == 1): return arr
    else: return arr[:1] + capitalizeFirst(arr[1:])


li = ['apple','banana','mango','pineapple']
print(capitalizeFirst(li))