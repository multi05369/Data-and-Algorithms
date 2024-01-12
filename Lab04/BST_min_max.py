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
            root = self.get_root()
            self.preorder(root)

    def is_empty(self):
        '''check BST is empty or not'''
        if self.get_root() is None:
            return True
        else:
            return False

    def inorder(self, root=None):
        '''traverse data by inordering'''
        if root != None:
            if root.get_left() != None:
                self.inorder(root.get_left())
            print("->", root.get_data(), end=" ")
            if root.get_right() != None:
                self.inorder(root.get_right())
        else:
            root = self.get_root()
            self.inorder(root)

    def postorder(self, root=None):
        '''traverse data by postordering'''
        if root != None:
            if root.get_left() != None:
                self.postorder(root.get_left())
            if root.get_right() != None:
                self.postorder(root.get_right())
            print("->", root.get_data(), end=" ")
        else:
            root = self.get_root()
            self.postorder(root)

    def traverse(self):
        '''traverse the data'''
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('\nInorder: ', end='')
        self.inorder()
        print('\nPostorder: ', end='')
        self.postorder()

    def find_max(self):
        '''find the biggest Node in the root'''
        pos = self.root
        while pos.right is not None:
            pos = pos.right
        return pos.data

    def find_min(self):
        '''fing the smallest Node in the root'''
        pos = self.root
        while pos.left is not None:
            pos = pos.left
        return pos.data

def main():
    '''solution'''
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("\nMax:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()
