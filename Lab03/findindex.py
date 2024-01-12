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
        if self.head is None:
            print("This is an empty list.")
            return
        current = self.head
        while current is not None:
            self.count -= 1
            if self.count == 0:
                print(current.get_data())
                current = current.get_next()
            else:
                print(current.get_data(), end=" -> ")
                current = current.get_next()

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
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def insert_before(self, node, data):
        '''insert the new node at the front of node by set'''
        new_node = DataNode(data)
        current = self.head
        prev = None

        if current is None:
            print("Cannot insert, %s does not exist." % node)
            return

        if current.get_data() == node:
            self.insert_front(data)
            return

        while current is not None and current.get_data() != node:
            prev = current
            current = current.get_next()

        if current is None:
            print("Cannot insert, %s does not exist." % node)
            return

        new_node.set_next(current)
        prev.set_next(new_node)
        self.count += 1

    def delete(self, data):
        '''delete the data from the Singly Linked List'''
        current = self.head
        prev = None

        if current is None:
            print("Cannot delete, %s does not exist." % data)
            return

        if current.get_data() == data:
            self.head = current.get_next()
            self.count -= 1
            return

        while current is not None and current.get_data() != data:
            prev = current
            current = current.get_next()

        if current is None:
            print("Cannot delete, %s does not exist." % data)
            return

        prev.set_next(current.get_next())
        self.count -= 1

def findindex():
    '''solution'''
    data = SinglyLinkedList()
    data_inserted = False
    while True:
        food = input()
        if food.capitalize() == "Last":
            break
        data.insert_last(food)
        data_inserted = True
    num_index = int(input())

    if not data_inserted:
        print("Error")
        return

    # Traverse part
    current = data.head
    index = 0

    while current is not None:
        index += 1
        if num_index <= 0:
            print("Error")
            break
        if index == num_index:
            print(current.get_data())
            break
        current = current.get_next()

    if index < num_index:
        print("Error")

findindex()
