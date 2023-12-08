'''function'''
class Person:
    '''learn how to OOP so F confused'''
    def __init__(self, name, age):
        '''main def? right'''
        self.name = name
        self.age = age

    def get_details(self):
        '''create details'''
        return "%s, %d years old" % (self.name, self.age)

    def say_hello(self):
        '''say hello function'''
        return "Hello, my name is %s!" % self.name

class Project:
    '''for building project?'''
    def __init__(self, projectName, member, listmem):
        '''Jinx?'''
        self.projectname = projectName
        self.member = member
        self.listmem = listmem

    def showprojectname(self):
        '''Say hello to my little friend!'''
        print("Hello There! This is %s" % self.projectname)

    def showmembers(self):
        '''BOOM!!!'''
        print("This project has %d members" % self.member)
        for name, age in self.listmem:
            person = Person(name, age)
            print(person.say_hello())

def main(projectname, members):
    '''main function'''
    memlist = []
    for _ in range(members):
        name = input()
        age = int(input())
        memlist.append((name, age))

    memlist.sort(key=lambda x: x[0])
    person = Project(projectname, members, memlist)
    person.showprojectname()
    person.showmembers()

main(input(), int(input()))
