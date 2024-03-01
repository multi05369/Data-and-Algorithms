'''function'''
import json
def insertionsort(list1, last):
    '''solution'''
    current = 1
    times = 0
    while current <= last:
        hold = list1[current]
        walker = current - 1
        while walker >= 0:
            times += 1
            if is_current_smaller(hold, list1[walker]):
                list1[walker + 1] = list1[walker]
                walker -= 1
            else:
                break
        list1[walker + 1] = hold
        current += 1
        print(list1)
    print("Comparison times: %d" % times)

def is_current_smaller(current, walker):
    '''check is it smaller?'''
    if current[0] == walker[0]:
        return int(current[1:]) < int(walker[1:])
    else:
        return current[0] < walker[0]

insertionsort(json.loads(input().replace("'", '"')), int(input()))
