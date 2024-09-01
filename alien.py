from turtle import Turtle
import random

# The initialized positions of alien ships
alien_pos_x = [-320 + 80 * i for i in range(9)]
alien_pos_y = [150 + 50 * i for i in range(6)]

# original_move_dir = [0, 180]


class Alien(Turtle):

    def __init__(self, cor):
        super().__init__()
        self.shape('./img/alien_ship.gif')
        self.penup()
        self.goto(cor)
        self.setheading(0)
        # self.x = cor[1]

    def move(self):
        self.forward(10)

    def rotate(self):
        self.right(180)

    def get_x_cor(self):
        return self.xcor()

    def remove(self):
        self.hideturtle()


class Aliens():
    def __init__(self):
        self.aliens_list = []
        self.quantity_list = []
        self.first_col = 0
        self.last_col = 0
        self.create_aliens()
        # self.quantity_list = [0, 0, 2, 0, 0, 0]   # for test

    # Create alien ships
    def create_aliens(self):
        for x in alien_pos_x:
            alien_y_list = []
            quantity_y = 0

            for y in alien_pos_y:
                alien_y_list.append(Alien(cor=(x, y)))
                quantity_y += 1
                # self.aliens_list.append(Alien(cor=(x, y)))
                # self.quantity += 1
            self.aliens_list.append(alien_y_list)
            self.quantity_list.append(quantity_y)

    # Get the x coordination of first columns of the rest of alien ships, in order to make aliens not out of the frame
    def get_first_col(self):
        for col in range(len(self.quantity_list)):
            # print(f"First >> col now: {col}")
            if self.quantity_list[col] > 0:
                self.first_col = col
                break
            self.first_col = 0

    # Get the x coordination of last columns of the rest of alien ships, in order to make aliens not out of the frame
    def get_last_col(self):
        for col in range(len(self.quantity_list)-1, -1, -1):
            # print(f"Last >> col now: {col}")
            if self.quantity_list[col] > 0:
                self.last_col = col
                break
            self.last_col = 0

    # Alien ships move
    def herd_move(self):
        if self.aliens_list[self.last_col][0].heading() == 0:
            if self.aliens_list[self.last_col][0].xcor() < 560:
                for alien_x in self.aliens_list:
                    for alien in alien_x:
                        alien.move()
            else:
                for alien_x in self.aliens_list:
                    for alien in alien_x:
                        alien.rotate()
        else:
            if self.aliens_list[self.first_col][0].xcor() > -560:
                for alien_x in self.aliens_list:
                    for alien in alien_x:
                        alien.move()
            else:
                for alien_x in self.aliens_list:
                    for alien in alien_x:
                        alien.rotate()

    # Remove alien ships from the lists once they were hit
    def remove_alien(self, col, alien):
        index = self.aliens_list[col].index(alien)
        self.aliens_list[col][index].remove()
        self.aliens_list[col].remove(alien)
        self.quantity_list[col] -= 1
        # print(self.quantity_list)
        # print(f"Alien List: {self.aliens_list}")




