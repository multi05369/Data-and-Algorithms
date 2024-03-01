'''function'''
class Item:
    '''collect the item from kun doubt'''
    def __init__(self, name, price, weight):
        '''public Item() {}'''
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        '''return the name'''
        return self.name

    def get_price(self):
        '''return the price'''
        return self.price


    def get_weight(self):
        '''return the weight'''
        return self.weight


    def get_cost(self):
        '''calculate the cost use greedy'''
        pass

def main():
    '''P Tae Tae sud tae'''
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
