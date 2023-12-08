'''https://open.spotify.com/track/5QO79kh1waicV47BqGRL3g?si=20bbff757f7b449e'''
def bangna_trad(kilo):
    '''solution'''
    if 0.000 <= kilo <= 5.032:
        return "Bangkok"
    elif 5.032 < kilo <= 35.477:
        return "Samut Prakarn"
    elif 35.477 < kilo <= 52.900:
        return "Chachoengsao"
    elif 52.900 < kilo <= 58.855:
        return "Chon Buri"
    else:
        return "InValid"

print(bangna_trad(float(input())))
