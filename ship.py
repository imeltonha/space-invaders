from turtle import Turtle


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('./img/ship.gif')
        self.penup()
        self.goto(0, -400)

    def get_x_cor(self):
        return self.xcor()

    def move_right(self):
        if self.xcor() < 580:
            self.setheading(0)
            self.forward(10)

    def move_left(self):
        if self.xcor() > -580:
            self.setheading(180)
            self.forward(10)


