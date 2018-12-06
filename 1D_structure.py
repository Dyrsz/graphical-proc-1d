import turtle
import random

# CONSTANTS
W = 15  # grid width
H = 15  # grid height
INIT_X = -30
INIT_Y = 17
SQUARE_LINE_LENGTH = 57
FILL_COLOR = "blue"
BORDER_COLOR = "black"
PEN_SIZE = 2
# Protected
_last_square_coord = 0, 0

# Window
win = turtle.Screen()
win.bgcolor("darkgrey")


# Classes
class Square:
    def __init__(self, line, column, filled):
        self.line = line
        self.column = column
        self.filled = filled
        self.x1 = (self.column + INIT_X)*W
        self.x2 = (self.column + INIT_X + 1)*W
        self.y1 = (self.line + INIT_Y)*H
        self.y2 = (self.line + INIT_Y + 1)*H
        self.draw(self.filled)

    def draw(self, filled=False):
        p = turtle.Turtle()
        p.hideturtle()
        p.speed(0)
        p.up()
        p.color = BORDER_COLOR
        p.fillcolor(FILL_COLOR)
        p.pensize(PEN_SIZE)
        p.goto(self.x2, self.y2)
        p.down()
        if filled:
            p.begin_fill()
        p.forward(W)
        p.left(90)
        p.forward(H)
        p.left(90)
        p.forward(W)
        p.left(90)
        p.forward(H)
        p.left(90)
        p.up()
        if filled:
            p.end_fill()
        global _last_square_coord
        _last_square_coord = p.position()

    def fill(self):
        self.filled = True

    def unfill(self):
        self.filled = False


class Line:
    def __init__(self, number, rules=None, init_rule=lambda: random.randint(0, 1)):
        self.number = number
        self.rules = rules
        self.init_rule = init_rule
        self.bool = []
        self.draw()

    def draw(self):
        for n in range(SQUARE_LINE_LENGTH):
            value = self.init_rule()
            Square(self.number, n, value)
            self.bool.append(value)


class Rule:
    def __init__(self, values, result):
        self.values = values
        self.result = result

    def draw(self, x, y):
        p = turtle.Turtle()
        p.hideturtle()
        p.speed(0)
        p.up()
        p.color = BORDER_COLOR
        p.pensize(PEN_SIZE)
        p.goto((7 + x + INIT_X) * W, (6.75 - y + INIT_Y) * H)
        p.write("1.", font=("Arial", 16, "normal"))
        for n in range(len(self.values)):
            Square(6 - y, 8 + n + x, self.values[n])
        draw_arrow_for_rule()
        for n in range(len(self.result)):
            Square(6 - y, 10 + n + x + len(self.values), self.result[n])


def draw_arrow_for_rule():
    p = turtle.Turtle()
    p.hideturtle()
    p.speed(0)
    p.up()
    p.goto(*_last_square_coord)
    p.left(20)
    p.forward(W + 0.5*H)
    p.down()
    p.color = BORDER_COLOR
    p.pensize(PEN_SIZE)
    p.right(20)
    p.forward(W)
    p.left(140)
    p.forward(0.3*W)
    p.back(0.3*W)
    p.right(280)
    p.forward(0.3*W)


def draw_rules(rules):
    p = turtle.Turtle()
    p.hideturtle()
    p.speed(0)
    p.up()
    p.color = BORDER_COLOR
    p.pensize(PEN_SIZE)
    p.goto((INIT_X + 1) * W, (INIT_Y + 7) * H)
    p.write("Reglas:", font=("Arial", 14, "normal"))
    p.up()
    for i in range(len(rules)):
        rules[i].draw(0, 0)


# ID de reglas.

r1 = Rule([1, 1], [0])
draw_rules([r1])
# r1.draw(1, 1)

l1 = Line(0)





turtle.done()
