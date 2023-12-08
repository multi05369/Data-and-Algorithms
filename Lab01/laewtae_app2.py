'''https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b?si=9c170ee965cd4b7d'''
class Laewtaeapp:
    '''application for random food'''
    def __init__(self, menu_food, random_times, new_list_food):
        '''constructor def'''
        self.menu_food = menu_food
        self.random_times = random_times
        self.new_list_food = new_list_food

    def random_foods(self):
        '''random food for eat'''
        return self.random_times + 1

    def list_foods(self):
        '''show all of the food that in the list'''
        return sorted(self.menu_food)

    def add_food_item(self):
        '''add food that user add'''
        self.menu_food += self.new_list_food
        return self.menu_food

def main(num):
    '''solution'''
    new_list_food = []
    for _ in range(num):
        food = input()
        new_list_food.append(food)
    menu = Laewtaeapp(["Fried Chicken", "Hamburger", "Pizza", "Steak"], 0, new_list_food)

    menu.add_food_item()
    print(menu.list_foods())

main(int(input()))
