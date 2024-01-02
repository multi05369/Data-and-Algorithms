'''function'''
class ArrayStack:
    '''how to array'''
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        '''pop the data'''
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            val = self.data[-1]
            self.data.pop()
            self.size -= 1
            return val

    def is_empty(self):
        '''check data is empty or not'''
        if self.size == 0:
            return True
        else:
            return False

    def get_stack_top(self):
        '''get the top of stack'''
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            return self.data[-1]

    def get_size(self):
        '''get the size of stack'''
        return self.size

    def print_stack(self):
        '''print the stack'''
        print(self.data)

def is_parentheses_matching():
    '''check is matching or not'''
    express = str(input())
    stack1 = ArrayStack()
    for i in express:
        if i == "(":
            stack1.push("(")
        elif i == ")":
            if stack1.get_size() == 0:
                print("Underflow: Cannot pop data from an empty list")
            else:
                stack1.pop()
    if (stack1.get_size() == 0 and "(" in express) or (stack1.get_size() == 0 \
        and "(" not in express and ")" not in express):
        print("Parentheses in %s are matched" % express)
        return True
    else:
        print("Parentheses in %s are unmatched" % express)
        return False

print(is_parentheses_matching())
