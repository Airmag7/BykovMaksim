class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def hoard(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        if self.state == 'C':
            self.state = 'G'
            return 6
        if self.state == 'D':
            self.state = 'E'
            return 7
        raise MealyError('hoard')

    def apply(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('apply')

    def peep(self):
        if self.state == 'A':
            self.state = 'A'
            return 2
        if self.state == 'G':
            self.state = 'H'
            return 10
        raise MealyError('peep')

    def grow(self):
        if self.state == 'B':
            self.state = 'C'
            return 4
        if self.state == 'A':
            self.state = 'G'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 8
        if self.state == 'G':
            self.state = 'E'
            return 11
        raise MealyError('grow')


def main():
    return StateMachine()


def test():
    o = main()
    o.peep()
    o.apply()
    o.grow()
    o.grow()
    o.hoard()
    o.grow()
    o.apply()
    o.grow()
    o.grow()
    o.apply()
    o.peep()
    o = main()
    o.grow()
    o.peep()
    o = main()
    o.hoard()
    o.grow()
    o.apply()
    o.peep()
    o = main()
    o.apply()
    o.grow()
    o.hoard()
    o.peep()
    try:
        o.peep()
    except MealyError:
        pass
    try:
        o.grow()
    except MealyError:
        pass
    try:
        o.apply()
    except MealyError:
        pass
    try:
        o.hoard()
    except MealyError:
        pass
