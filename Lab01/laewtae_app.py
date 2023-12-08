'''https://open.spotify.com/track/1fDFHXcykq4iw8Gg7s5hG9?si=d1a4043d0e4f4223'''
class Laewtaeapp:
    '''application for random food'''
    def __init__(self, menu_food, random_times):
        '''constructor def'''
        self.menu_food = menu_food
        self.random_times = random_times

    def random_foods(self):
        '''random food for eat'''
        return self.random_times + 1

    def list_foods(self):
        '''show all of the food that in the list'''
        return sorted(self.menu_food)

def main():
    '''solution'''
    menu = Laewtaeapp(["Pizza", "Fried Chicken", "Hamburger", "Steak"], 0)
    print(menu.list_foods())

main()
