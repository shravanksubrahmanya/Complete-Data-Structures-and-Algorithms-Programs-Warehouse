'''
This program demonstrates the solving longest common subsequence problem using divide 
and conquer approach
'''

def findLCS(s1,s2,index1 = 0, index2 = 0):
    if index1 >= len(s1) or index2 >= len(s2):
        return 0
    elif s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1 + 1, index2 + 1)
    else:
        option1 = findLCS(s1, s2, index1 + 1, index2)
        option2 = findLCS(s1, s2, index1, index2 + 1)
        return max(option1, option2)

print(findLCS('elephant','elrphalt'))