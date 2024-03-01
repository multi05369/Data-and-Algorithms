'''function'''
class Student:
    '''Student narak'''
    def __init__(self, idd, namee, gpaa):
        '''constructor def'''
        self.std_id = idd
        self.name = namee
        self.gpa = gpaa

    def get_std_id(self):
        '''return the std_id'''
        return self.std_id

    def get_name(self):
        '''return the name'''
        return self.name

    def get_gpa(self):
        '''return the gpa'''
        return self.gpa

    def print_detail(self):
        '''print the details about std_id, name and gpa'''
        print("ID: %s" % self.get_std_id())
        print("Name: %s" % self.get_name())
        print("GPA: %.2f" % self.get_gpa())

def main(text_in):
    """I love Laew Tae App"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())
