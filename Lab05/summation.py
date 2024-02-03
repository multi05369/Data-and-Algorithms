'''function'''
def summation(num):
    '''solution'''
    ans = 0
    for i in range(1, num + 1):
        ans += i
    print(ans)
summation(int(input()))
