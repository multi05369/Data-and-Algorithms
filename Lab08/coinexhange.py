'''function'''
import json
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def coinexchange():
    '''solution'''
    amt = int(input())
    temp = amt
    data = convert_key(json.loads(input()))
    print("Amount: {}".format(temp))
    res = 0
    dct_coin = {10: 0, 5: 0, 2: 0, 1: 0}

    for i in sorted(data.keys(), reverse=True):
        coin = min(amt // i, data[i])
        if coin > 0:
            res += coin
            amt -= coin * i
            data[i] -= coin
            dct_coin[i] += coin
        if amt == 0:
            break

    if amt == 0:
        print("Coin exchange result:")
        for coin in dct_coin.keys():
            count = dct_coin[coin]
            print("  {} baht = {} coins".format(coin, count))
        print("Number of coins: {}".format(res))
    else:
        print("Coins are not enough.")
coinexchange()
