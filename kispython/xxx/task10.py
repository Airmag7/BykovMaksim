class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def leer(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 6
        if self.state == 'B':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'G'
            return 9
        raise MealyError('leer')

    def pose(self):
        if self.state == 'A':
            self.state = 'D'
            return 2
        if self.state == 'B':
            self.state = 'G'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 8
        if self.state == 'F':
            self.state = 'G'
            return 10
        if self.state == 'G':
            self.state = 'H'
            return 11
        raise MealyError('pose')

    def trim(self):
        if self.state == 'B':
            self.state = 'C'
            return 3
        if self.state == 'A':
            self.state = 'H'
            return 1
        if self.state == 'D':
            self.state = 'E'
            return 7
        raise MealyError('trim')


def main():
    return StateMachine()


def test():
    o = main()
    o.leer()
    o.pose()
    o.pose()
    o = main()
    o.leer()
    o.leer()
    o.pose()
    o.pose()
    o.pose()
    o = main()
    o.leer()
    o.trim()
    o.leer()
    o.trim()
    o.leer()
    o.pose()
    o = main()
    o.trim()
    o = main()
    o.pose()
    o.trim()
    o.leer()
    o.pose()
    try:
        o.leer()
    except MealyError:
        pass
    try:
        o.trim()
    except MealyError:
        pass
    try:
        o.pose()
    except MealyError:
        pass
