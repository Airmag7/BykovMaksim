class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def move(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 8
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('move')

    def zoom(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        if self.state == 'B':
            self.state = 'F'
            return 4
        if self.state == 'C':
            self.state = 'G'
            return 6
        raise MealyError('zoom')

    def scan(self):
        if self.state == 'A':
            self.state = 'E'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 5
        if self.state == 'D':
            self.state = 'E'
            return 7
        raise MealyError('scan')


def main():
    return StateMachine()


def test():
    o = main()
    o.scan()
    o.move()
    o.move()
    o = main()
    o.zoom()
    o.scan()
    o.scan()
    o.move()
    o.move()
    o = main()
    o.move()
    o.move()
    o.zoom()
    o = main()
    o.move()
    o.zoom()
    o.move()
    try:
        o.zoom()
    except MealyError:
        pass
    try:
        o.move()
    except MealyError:
        pass
    try:
        o.scan()
    except MealyError:
        pass
