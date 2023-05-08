class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def punch(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'F'
            return 5
        if self.state == 'G':
            self.state = 'H'
            return 10
        raise MealyError('punch')

    def turn(self):
        if self.state == 'A':
            self.state = 'H'
            return 1
        if self.state == 'C':
            self.state = 'H'
            return 6
        if self.state == 'D':
            self.state = 'E'
            return 7
        raise MealyError('turn')

    def spawn(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 4
        raise MealyError('spawn')

    def paint(self):
        if self.state == 'B':
            self.state = 'F'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 8
        if self.state == 'F':
            self.state = 'G'
            return 9
        if self.state == 'G':
            self.state = 'D'
            return 11
        raise MealyError('paint')


def main():
    return StateMachine()


def test():
    o = main()
    o.punch()
    o.spawn()
    o.punch()
    o.paint()
    o.paint()
    o.turn()
    o.paint()
    o.paint()
    o.punch()
    try:
        o.punch()
    except MealyError:
        pass
    o = main()
    o.turn()
    try:
        o.turn()
    except MealyError:
        pass
    o = main()
    o.punch()
    o.paint()
    o.paint()
    o.punch()
    try:
        o.paint()
    except MealyError:
        pass
    o = main()
    o.punch()
    o.spawn()
    o.turn()
    try:
        o.spawn()
    except MealyError:
        pass
    o = main()
    o.punch()
    o.spawn()
    o.spawn()
