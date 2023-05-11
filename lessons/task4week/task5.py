from IPython.display import display


class SVG:
    def __init__(self):
        self.lines = []
        self.circles = []
        self.width = 0
        self.height = 0

    def line(self, x1, y1, x2, y2, color='black'):
        self.lines.append((x1, y1, x2, y2, color))
        self.width = max(self.width, x1, x2)
        self.height = max(self.height, y1, y2)

    def circle(self, cx, cy, r, color='black'):
        self.circles.append((cx, cy, r, color))
        self.width = max(self.width, cx + r)
        self.height = max(self.height, cy + r)

    def save(self, filename, width=None, height=None):
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        with open(filename, 'w') as f:
            f.write(
                '<svg version="1.1" width="{:.6f}" height="{:.6f}" xmlns="http://www.w3.org/2000/svg">\n'.format(width,
                                                                                                                 height))
            for x1, y1, x2, y2, color in self.lines:
                f.write('<line x1="{:.6f}" y1="{:.6f}" x2="{:.6f}" y2="{:.6f}" stroke="{}" />\n'.format(x1, y1, x2, y2,
                                                                                                        color))
            for cx, cy, r, color in self.circles:
                f.write('<circle cx="{:.6f}" cy="{:.6f}" r="{:.6f}" fill="{}" />\n'.format(cx, cy, r, color))
            f.write('</svg>')


svg = SVG()

svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0
        self.width = 0

    def set_pos(self, start_x=0, start_y=0, scale_x=0):
        if self.left is not None:
            self.left.set_pos(start_x, start_y + 1)
            self.x = (self.left.x + scale_x + max(self.left.width, self.right.width)) / 2
        else:
            self.x = start_x
        if self.right is not None:
            self.right.set_pos(self.x + scale_x, start_y + 1)
        else:
            self.width = scale_x
        if self.left is None and self.right is None:
            self.width = scale_x
        else:
            self.width = self.right.x - self.left.x

    def draw(self, svg, scale_y):
        x1 = self.x - self.width / 2
        y1 = self.y * scale_y
        x2 = self.x + self.width / 2
        y2 = (self.y + 1) * scale_y

        if self.left is not None:
            svg.line(self.x, y1, self.left.x, y2)
        if self.right is not None:
            svg.line(self.x, y1, self.right.x, y2)

        svg.circle(self.x, y1, r=10, color='red')
        # svg.text(self.x, y1, self.val, size=20)


# пример использования

tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
t = Tree(1, tree_2, tree_8)
t.set_pos()
svg = SVG()
t.draw(svg)
svg.save('tree.svg', width=500, height=200)
display(svg)
