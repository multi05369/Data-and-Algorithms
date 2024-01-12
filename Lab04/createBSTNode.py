'''function'''
class BSTNode:
    '''How to BST Code eiei'''
    def __init__(self, data):
        '''constructure def'''
        self.data = int(data)
        self.left = None
        self.right = None

    def get_data(self):
        '''get the data'''
        return self.data

    def set_data(self, data):
        '''set the data'''
        self.data = data

    def get_left(self):
        '''get the data from left'''
        return self.left

    def set_left(self, left):
        '''set the data at left'''
        self.left = left

    def get_right(self):
        '''get the data from right'''
        return self.right

    def set_right(self, right):
        '''set the data at right'''
        self.right = right

def main(data):
    '''solution'''
    new_node = BSTNode(data)
    print(new_node.get_data())
    print(new_node.get_left())
    print(new_node.get_right())

main(int(input()))
