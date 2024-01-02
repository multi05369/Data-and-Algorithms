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

def infixtopostfix(expression):
    '''solution'''
    stack1 = ArrayStack()
    res = []
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for i in expression:
        if i in "+-*/":
            while not stack1.is_empty() and \
                operator_precedence.get(stack1.get_stack_top(), 0) >= \
                operator_precedence.get(i, 0):
                res.append(stack1.pop())
            stack1.push(i)
        else:
            res.append(i)

    while not stack1.is_empty():
        res.append(stack1.pop())

    print("".join(res).replace(" ", ""))


infixtopostfix(str(input()).strip(""))
