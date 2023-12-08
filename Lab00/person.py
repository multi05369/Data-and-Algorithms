'''function'''
class Person:
    '''learn how to OOP so F confused'''
    def __init__(self, name, age):
        '''main def? right'''
        self.name = name
        self.age = age
        print(self.get_details())
        print(self.say_hello())

    def get_details(self):
        '''create details'''
        return "%s, %d years old" % (self.name, self.age)

    def say_hello(self):
        '''say hello function'''
        return "Hello, my name is %s!" % self.name

Person(input(), int(input()))
