'''function'''
import json
def isintersect():
    '''solution'''
    list1 = json.loads(input())
    list2 = json.loads(input())
    list3 = json.loads(input())
    for i in list1:
        if i in list2 and i in list3:
            print(True)
            break
        else:
            print(False)
            break
isintersect()
