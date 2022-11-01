'''
This program demonstrates the reversing of a string using recursion method
'''

def revStr(s):
    ns = ''
    if len(s) <= 1:
        return s
    else:
        return s[-1] + revStr(s[:-1])
        
print(revStr("Hello"))