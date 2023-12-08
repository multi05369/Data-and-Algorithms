'''re build the code'''
class Person:
    '''class for create an object of pesron'''
    def __init__(self, name, age):
        '''like a main def I think'''
        self.name = name # mean create a object name "name"
        self.age = age #mena create a object name "age"

    def get_details(self):
        '''function for create a detail'''
        print("%s, %d years old" % (self.name, self.age))

    def say_hello(self):
        '''function for say hello'''
        print("Hello, my name is %s!" % self.name)

def main(name, age):
    '''function main I don't know what name it should be so this is basic'''
    person = Person(name, age) # send name and age into the class Person
    person.get_details() # call function
    person.say_hello() # call function

main(input(), int(input()))
