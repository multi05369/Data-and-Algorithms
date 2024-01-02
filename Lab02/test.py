class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
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
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            val = self.data[-1]
            self.data.pop()
            self.size -= 1
            return val

    def is_empty(self):
        return self.size == 0

    def get_stack_top(self):
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            return self.data[-1]

    def get_size(self):
        return self.size

    def print_stack(self):
        print(self.data)


def is_valid_expression(express):
    stack1 = ArrayStack()
    brackets = {'(': ')', '[': ']', '{': '}'}

    for i in express:
        if i in brackets:
            stack1.push(i)
        elif i in brackets.values():
            if stack1.is_empty() or brackets[stack1.get_stack_top()] != i:
                print("Underflow: Cannot get stack top from an empty list")
                return False
            stack1.pop()

    if stack1.is_empty():
        return True
    else:
        return False


expression = str(input("Enter the expression: "))
print(is_valid_expression(expression))
