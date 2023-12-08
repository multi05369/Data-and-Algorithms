'''function'''
class Point:
    '''calculate distance'''
    def __init__(self, x=0, y=0):
        '''constructir def'''
        self.set_coordinates(x, y)

    def set_coordinates(self, xxx, yyy):
        '''set the pos'''
        self.xxx = xxx
        self.yyy = yyy

    def get_coordinates(self):
        '''get the pos'''
        return (self.xxx, self.yyy)

    def calculate_distance(self, other_point):
        '''calculating'''
        return ((other_point.xxx - self.xxx)**2 + (other_point.yyy - self.yyy)**2) ** 0.5

def main():
    '''solution'''
    boss = Point(float(input()), float(input()))
    art = Point(float(input()), float(input()))

    res = boss.calculate_distance(art)
    print("%.2f" % res)

main()
