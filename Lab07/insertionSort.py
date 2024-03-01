'''function'''
import json
def insertionsort(list1, last):
    '''solution'''
    count1 = 0
    count2 = 0
    for current in range(1, last + 1):
        hold = list1[current]
        walker = current - 1
        count1 += 1
        while walker >= 0 and hold < list1[walker]:
            list1[walker + 1] = list1[walker]
            walker -= 1
            count2 += 1
        list1[walker + 1] = hold
        print(list1)
    print("Comparison times: %d" % max(count1, count2))


insertionsort(json.loads(input()), int(input()))
