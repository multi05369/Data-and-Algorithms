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

def main(name):
    '''solution'''
    pnew = DataNode(name)
    print(pnew.get_data())
    print(pnew.get_next())

main(str(input()))
