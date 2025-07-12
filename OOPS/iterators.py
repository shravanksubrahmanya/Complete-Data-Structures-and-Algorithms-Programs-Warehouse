l = [4,2,6,3,1,5]

iterator = iter(l)

print("Type of iterator:", type(iterator))
print(iterator)

next(iterator)  # Get the first element
print(next(iterator))  # Get the second element
print(next(iterator))  # Get the third element
print(next(iterator))  # Get the fourth element
print(next(iterator))  # Get the fifth element
print(next(iterator))  # Raises StopIteration if there are no more elements
print(next(iterator, "No more elements"))  # Returns default value if no more elements

# generator
def square(n):
    for i in range(n):
        yield i * i
    
gen = square(3)
print("Type of generator:", type(gen))
print(gen)
print(next(gen))  # Get the first square
print(next(gen))  # Get the second square
print(next(gen))  # Get the third square
print(next(gen, "No more squares"))  # Returns default value if no more squares
print("Type of generator after exhaustion:", type(gen))