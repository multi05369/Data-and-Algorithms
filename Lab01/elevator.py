'''function'''
class Elevator:
    '''building elevator system'''
    def __init__(self, max_floor):
        '''constructor def'''
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        '''calculate floor'''
        if floor > self.max_floor:
            print("Invalid Floor!")
        else:
            self.current_floor = floor

    def report_current_floor(self):
        '''report the result'''
        print(self.current_floor)

def main():
    '''solution'''
    elevator = Elevator(int(input()))
    while True:
        check = input()
        if check == "Done":
            elevator.report_current_floor()
            break
        else:
            elevator.go_to_floor(int(check))

main()
