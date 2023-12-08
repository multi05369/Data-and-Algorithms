'''function'''
def selection(num):
    '''solution'''
    list1 = []
    for _ in range(int(num)):
        name = input()
        list1.append(name)

    for i in range(len(list1) - 1):
        less = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[less]:
                less = j
        list1[i], list1[less] = list1[less], list1[i]

    for n_list in list1:
        print(n_list)

selection(float(input()))
