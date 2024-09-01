from turtle import Turtle


class Barrier(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('gray')
        self.goto(cor)


# class Barriers():
#     def __init__(self):
#         self.barriers_list = []
#         self.