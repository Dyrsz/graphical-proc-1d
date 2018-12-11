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
_last_line_bools = []

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


def generate_init_line(number_squares_filled, patron=None):
    if patron is not None:
        return patron*(SQUARE_LINE_LENGTH//patron + 1)[0:SQUARE_LINE_LENGTH]  # Mejorable.
    else:
        return [1] * number_squares_filled + [0] * (SQUARE_LINE_LENGTH - number_squares_filled)


class Line:
    def __init__(self, number, rules, use_init_rule=True, init_line=None,
                 init_rule=lambda: random.randint(0, 1)):
        self.number = number
        self.rules = rules
        self.use_init_rule = use_init_rule
        self.init_rule = init_rule
        self.init_line = init_line
        self.bool = []
        self.draw()

    def draw(self):
        for n in range(SQUARE_LINE_LENGTH):
            if self.number == 0:
                if self.use_init_rule:
                    value = self.init_rule()
                else:
                    if self.init_line is None:
                        raise Exception("Init line does not exists.")
                    if not isinstance(self.init_line, list):
                        raise Exception("Init line must be a list.")
                    if len(self.init_line) != SQUARE_LINE_LENGTH:
                        raise Exception("Init line has a wrong length.")
                    value = self.init_line[n]
                Square(-self.number, n, value)
                self.bool.append(value)
            else:
                global _last_line_bools
                model = _last_line_bools
                print(model)
                count = 0
                for rule in self.rules:
                    if rule.values == model[n:len(rule.values)]:
                        if len(rule.result) == 1:
                            value = rule.result
                            Square(-self.number, n, value)
                            self.bool.append(value)
                            break
                        else:
                            values = rule.result
                            to_add = len(values)
                            excent = to_add + n
                            if excent > SQUARE_LINE_LENGTH:
                                to_add = SQUARE_LINE_LENGTH - n
                            for m in range(to_add):
                                Square(-self.number, n+m, values[m])
                                self.bool.append(values[m])
                            n += to_add
                            break
                    else:
                        count += 1
                if count == len(self.rules):
                    Square(-self.number, n, False)
                    self.bool.append(False)
        _last_line_bools = self.bool


class Rule:
    def __init__(self, values, result, number):
        self.values = values
        self.result = result
        self.number = number

    def draw(self, x, y):
        p = turtle.Turtle()
        p.hideturtle()
        p.speed(0)
        p.up()
        p.color = BORDER_COLOR
        p.pensize(PEN_SIZE)
        p.goto((7 + 6*x + INIT_X) * W, (6.75 - y + INIT_Y) * H)
        p.write(str(self.number) + ".", font=("Arial", 16, "normal"))
        for n in range(len(self.values)):
            Square(6 - 2*y, 8 + n + 6*x, self.values[n])
        for n in range(len(self.result)):
            Square(5 - 2*y, 8 + n + 6*x, self.result[n])


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
        rules[i].draw(i, 0)


# ID de reglas.

r1 = Rule([1, 1, 0], [1], 1)
r2 = Rule([0, 0], [1, 1], 2)
my_rules = [r1, r2]
draw_rules(my_rules)

l1 = Line(0, None, False, generate_init_line(5))
l2 = Line(1, my_rules)




turtle.done()
