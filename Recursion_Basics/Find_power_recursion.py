# this program is used to find the power of a number using recursion method

def Find_power(base, exponent):
    assert base > 0 and exponent >=0, 'Enter valid value for Base and Exponent'
    if exponent == 0: return 1
    else: return base * Find_power(base, exponent -1)

print(Find_power(2,9))

