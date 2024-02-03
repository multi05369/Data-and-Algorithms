'''function'''
def calculator(num):
    '''solution'''
    if num == 1:
        return 1

    num_str = str(num)
    digits = len(num_str)
    press = 0
    for i in range(1, digits):
        press += i * (9 * (10 ** (i - 1)))
    press += digits * (num - 10 ** (digits - 1) + 1) + num
    print(press)

calculator(int(input()))
