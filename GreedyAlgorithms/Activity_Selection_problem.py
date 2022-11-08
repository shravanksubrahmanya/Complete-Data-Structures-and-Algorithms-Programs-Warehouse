'''
This algorithm demonstrates the activity selection problem based on greedy approach
this algorithm focuses on completing maximum number of activity in a given list of activities
'''

def SelectMaxActivities(Activities):
    Activities.sort(key = lambda x: x[2])

    # printing out the first activity because it is earliest finishing activity
    print(Activities[0][0])
    prevEndTime = Activities[0][2]

    for i in range(1,len(Activities)):
        currentStartTime = Activities[i][1]
        currentEndTime = Activities[i][2]
        if currentStartTime >= prevEndTime:
            print(Activities[i][0])
            prevEndTime = currentEndTime

Activities = [
    ['A1',0,6],
    ['A2',3,4],
    ['A3',1,2],
    ['A4',5,8],
    ['A5',5,7],
    ['A6',8,9]
]

SelectMaxActivities(Activities)
