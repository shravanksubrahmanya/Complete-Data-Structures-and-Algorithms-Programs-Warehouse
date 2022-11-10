'''
This program demonstrates the longest palindromic subsequence problem using divide and 
conquer approach
'''

def findLPS(string, startindex, endindex):
    if startindex > endindex:
        return 0
    elif startindex == endindex:
        return 1
    elif string[startindex] == string[endindex]:
        return 2 + findLPS(string, startindex + 1, endindex - 1)
    else:
        option1 = findLPS(string, startindex, endindex - 1)
        option2 = findLPS(string, startindex + 1, endindex)
        return max(option1, option2)

string = 'ELRMENMET'
print(findLPS(string, 0, len(string) - 1))