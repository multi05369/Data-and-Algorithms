'''function'''
def rainy():
    '''solution 480 min = 8 hr 240 min = 4 hr'''
    status = input() # Indoor or Outdoor
    next_rain = float(input()) # in minute
    if status == "Indoor" and next_rain >= 480:
        print(True)
    elif status == "Indoor" and next_rain < 480:
        print(False)

    if status == "Outdoor" and next_rain >= 240:
        print(True)
    elif status == "Outdoor" and next_rain < 240:
        print(False)

rainy()
