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

class ProbHash:
    '''Probabilities?'''
    def __init__(self, size):
        '''constructor def'''
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key):
        '''hash the key by Modulo-division'''
        return key % self.size

    def rehash(self, key):
        '''return the rehash use when hash is not fit in'''
        return (key + 1) % (self.size)

    def insert_data(self, std):
        '''insert the data in hash table'''
        hash_num = self.hash(std.get_std_id())
        if self.hash_table[hash_num] is None:
            self.hash_table[hash_num] = std
            print("Insert %s at index %d" % (std.get_std_id(), hash_num))
        else:
            rehash_num = hash_num
            while self.hash_table[rehash_num] is not None:
                rehash_num = self.rehash(rehash_num)
                if rehash_num == hash_num:
                    print("The list is full. %s could not be inserted." % std.get_std_id())
                    break
            else:
                self.hash_table[rehash_num] = std
                print("Insert %s at index %d" % (std.get_std_id(), rehash_num))

    def search_data(self, std_id):
        '''search the data in the hash table'''
        hash_num = self.hash(std_id)
        index = hash_num
        while self.hash_table[index] is not None:
            if self.hash_table[index].get_std_id() == std_id:
                print("Found %s at index %d" % (std_id, index))
                return self.hash_table[index]
            index = self.rehash(index)
            if index == hash_num:
                break
        print("%s does not exist." % std_id)

def main():
    '''solution'''
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()
