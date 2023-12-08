'''function'''
def convert_string_to_tuples(text_in):
    '''swap case'''
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

def main(text):
    '''solution'''
    res = convert_string_to_tuples(text)
    first = res[0]
    last = res[1]
    first, last = last, first
    ans = (first, last)
    print(ans)

main(input())
