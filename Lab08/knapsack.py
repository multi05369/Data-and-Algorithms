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
        return self.price / self.weight

def knapsack(items, knap_cap):
    '''calculate greedy'''
    cap_check = 0
    print("Knapsack Size: {} kg".format(knap_cap))
    print("===============================")
    total = 0
    cur = 0
    res = []
    sort_items = sorted(items, key=lambda x: x.get_cost(), reverse=True)
    for i in sort_items:
        cur = cap_check + i.get_weight()
        if cur <= knap_cap:
            cap_check += i.get_weight()
            total += i.get_price()
            res.append(i)
        else:
            break
    for item in res:
        print("{} -> {} kg -> {} THB".format(item.get_name(), item.get_weight(), item.get_price()))
    print("Total: {} THB".format(total))

def main():
    '''solution'''
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)

main()
