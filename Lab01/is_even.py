'''function'''
def is_even(num):
    '''solution'''
    lastdigit = ['0', '2', '4', '6', '8']
    num = str(num)
    if num[-1] in lastdigit:
        return True
    else:
        return False

print(is_even(int(input())))
