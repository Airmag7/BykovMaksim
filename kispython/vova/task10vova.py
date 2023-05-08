class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def drive(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'G'
            return 2
        if self.state == 'C':
            self.state = 'F'
            return 4
        if self.state == 'E':
            self.state = 'C'
            return 7
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'G':
            self.state = 'H'
            return 9
        raise MealyError('drive')

    def color(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'G':
            self.state = 'G'
            return 10
        raise MealyError('color')

    def trash(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 6
        if self.state == 'G':
            self.state = 'E'
            return 11
        raise MealyError('trash')


def main():
    return StateMachine()


def test():
    o = main()
    o.drive()
    o.drive()
    o.color()
    o.trash()
    o.drive()
    o.trash()
    o.drive()
    o.trash()
    o.drive()
    o.drive()
    o = main()
    o.drive()
    o.color()
    o.drive()
    o.drive()
    o.drive()
    try:
        o.drive()
    except MealyError:
        pass
    try:
        o.color()
    except MealyError:
        pass
    try:
        o.trash()
    except MealyError:
        pass
