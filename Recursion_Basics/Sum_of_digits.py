# Program to find the sum of digits of a positive integer number using recursion

def Sum_digits(n):
    if n == 0:
        return 0
    else:
        # n % 10 used to get last digit of a number
        # n // 10 used to pass quotient to the recursion function
        return (n % 10 ) + Sum_digits(n // 10)

print(Sum_digits(145))