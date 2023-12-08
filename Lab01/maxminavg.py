'''function'''
import json
def findaverage():
    '''solution'''
    data = json.loads(input())
    lenght = len(data)
    res = 0
    less = data[0]
    most = 0
    for i in data:
        if i > most:
            most = i
    for j in data:
        if j < less:
            less = j
    for value in data:
        res += value
    average = res / lenght
    average = round(average, 2)
    ans = (most, less, average)
    print(ans)

findaverage()
