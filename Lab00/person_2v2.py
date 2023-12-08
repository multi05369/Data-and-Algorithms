'''function'''
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
        return "Hello, my name is %s!" % self.name

class Project:
    '''class for create an object of project'''
    def __init__(self, projectname, members, listmem):
        '''main fucntion'''
        self.projectname = projectname
        self.members = members
        self.listmem = listmem

    def showprojectname(self):
        '''create project name'''
        print("Hello There! This is %s" % self.projectname)

    def showmembers(self):
        '''create name of members by sorted'''
        print("This project has %d members" % self.members)
        for name, age in self.listmem:
            person = Person(name, age)
            print(person.say_hello())

def project_mem(projectname, num_mem):
    '''for call function'''
    memlist = [] # for append name and age
    for _ in range(num_mem):
        name = input()
        age = int(input())
        memlist.append((name, age))

    memlist.sort(key=lambda x: x[0]) # mean sort by x in index 0
    mem_of_pro = Project(projectname, num_mem, memlist)
    mem_of_pro.showprojectname()
    mem_of_pro.showmembers()

project_mem(input(), int(input()))
