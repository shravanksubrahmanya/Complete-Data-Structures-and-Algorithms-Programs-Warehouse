def Factorial(n):
    # assertion error will be thrown if the number is not an integer or a negative number
    assert n>=0 and int(n)==n, 'value should be a positive integer'
    
    if n == 0: return 1
    else: return n * Factorial(n-1)

n = int(input("Enter number : "))
print(Factorial(n))