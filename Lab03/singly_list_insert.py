'''fucntion'''
class DataNode:
    '''how to DataNode eiei'''
    def __init__(self, data):
        '''constructor def'''
        self.__data = data
        self.__next = None

    def get_data(self):
        '''return the data'''
        return self.__data

    def set_data(self, data):
        '''set the data'''
        self.__data = data

    def get_next(self):
        '''assign the data'''
        return self.__next

    def set_next(self, nextt=None):
        '''set the next node'''
        self.__next = nextt

class SinglyLinkedList:
    '''create a SinglyLinkedList'''
    def __init__(self):
        '''constructor def'''
        self.count = 0
        self.head = None

    def traverse(self):
        '''traverse in the list'''
        current = self.head
        if current is None:
            print("This is an empty list.")
            return
        output = ""
        while current is not None:
            output += current.get_data()
            if current.get_next() is not None:
                output += " -> "
            current = current.get_next()
        print(output)

    def insert_last(self, data):
        '''insert the new Node in the last'''
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.count += 1

    def insert_front(self, data):
        '''insert the new Node in the front'''
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

LIST1_ = SinglyLinkedList()
for _ in range(int(input())):
    TEXT_ = input()
    CONDI_, DATA_ = TEXT_.split(": ")
    if CONDI_ == "F":
        LIST1_.insert_front(DATA_)
    elif CONDI_ == "L":
        LIST1_.insert_last(DATA_)
    else:
        print("Invalid Condition!")
LIST1_.traverse()
