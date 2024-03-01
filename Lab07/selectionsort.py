'''function'''
import json
def selectionsort(list1, last):
    '''solution'''
    current = 0
    times = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if list1[walker] < list1[smallest]:
                smallest = walker
            times += 1
            walker += 1
        list1[current], list1[smallest] = list1[smallest], list1[current]
        current += 1
        print(list1)
    print("Comparison times: %d" % times)


selectionsort(json.loads(input()), int(input()))
