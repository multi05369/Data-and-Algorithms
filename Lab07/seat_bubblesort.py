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
            letter, num = list1[walker][0], int(list1[walker][1:])
            let_prev, num_prev = list1[walker - 1][0], int(list1[walker - 1][1:])
            if letter < let_prev or (letter == let_prev and num < num_prev):
                sortedd = False
                list1[walker], list1[walker - 1] = list1[walker - 1], list1[walker]
            count += 1
            walker -= 1
        current += 1
        print(list1)
    print("Comparison times: %d" % count)

bubblesort(json.loads(input().replace("'", '"')), int(input()))
