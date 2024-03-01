'''function'''
def stardust(num):
    '''solution'''
    lst = []
    med = 0
    for _ in range(num):
        src = int(input())
        lst.append(src)
    lst.sort()
    mean = sum(lst) / num

    if num % 2 == 0:
        med1 = lst[num // 2 - 1]
        med2 = lst[num // 2]
        med = (med1 + med2) / 2
    else:
        med = lst[num // 2]

    lstpow2 = [(x - mean)**2 for x in lst]
    std = (sum(lstpow2) / (num))**0.5

    print("%.2f" % mean)
    print("%.2f" % med)
    print("%.2f" % std)

stardust(int(input()))
