'''function'''
import json
def bubblesort(list1, last):
    '''solution'''
    current = 0
    sortedd = False
    count = 0
    while current <= last and sortedd == False:
        walker = last
        sortedd = True
        while walker > current:
            if list1[walker] < list1[walker - 1]:
                sortedd = False
                list1[walker], list1[walker - 1] = list1[walker - 1], list1[walker]
            count += 1
            walker -= 1
        current += 1
        print(list1)
    print("Comparison times: %d" % count)

bubblesort(json.loads(input()), int(input()))
