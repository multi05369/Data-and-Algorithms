'''function'''
class Rectangle:
    '''building a Rectangle'''
    def __init__(self, height, width):
        '''constructor def'''
        self.height = height
        self.width = width

    def calculate_area(self):
        '''for calculating'''
        return self.height * self.width

    def calculate_perimeter(self):
        '''for calculating'''
        return 2 * (self.height + self.width)

def main():
    '''solution'''
    rectangle = Rectangle(float(input()), float(input()))

    condition = input()
    if condition == "area":
        res = rectangle.calculate_area()
    else:
        res = rectangle.calculate_perimeter()

    print("%.2f" % res)

main()
