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

class BST:
    '''BST Node'''
    def __init__(self):
        '''constructure def'''
        self.root = None

    def get_root(self):
        '''get the root'''
        return self.root

    def set_root(self, root):
        '''set the root'''
        self.root = root

    def insert(self, data):
        '''insert the data in root'''
        new_node = BSTNode(data)
        if self.root is None:
            self.set_root(new_node)
        else:
            start = self.get_root()
            while True:
                if data < start.get_data():
                    if start.get_left() is None:
                        start.set_left(new_node)
                        break
                    start = start.get_left()
                else:
                    if start.get_right() is None:
                        start.set_right(new_node)
                        break
                    start = start.get_right()

    def preorder(self, root=None):
        '''traverse the data by preordering'''
        if root != None:
            print("->", root.get_data(), end=" ")
            if root.get_left() != None:
                self.preorder(root.get_left())
            if root.get_right() != None:
                self.preorder(root.get_right())
        else:
            root = self.root
            self.preorder(root)

def main():
    '''solution'''
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()
