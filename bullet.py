from turtle import Turtle
import random


colors = ['red', 'yellow', 'white', 'blue']
x_pos = [-320 + 80 * i for i in range(9)]


class Bullet(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1.2, stretch_wid=0.2)
        # self.color('red')
        self.color(random.choice(colors))
        self.penup()
        self.goto(cor)
        self.speed(0)

    def move(self):
        self.setheading(90)
        self.forward(20)

    def remove(self):
        self.hideturtle()


class Bullets():
    def __init__(self):
        self.bullets_list = []

    # Create bullet
    def create_bullet(self, ship_x):
        self.bullets_list.append(Bullet(cor=(ship_x, -360)))

    # Remove bullet once it hits other objects or out of the frame
    def remove_bullet(self, bullet):
        index = self.bullets_list.index(bullet)
        self.bullets_list[index].remove()
        self.bullets_list.remove(bullet)

    # # Reset(Remove) all the bullets from list when the ship is hit.
    # def reset_bullets(self):
    #     self.bullets_list = []