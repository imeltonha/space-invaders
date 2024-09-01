from turtle import Turtle


class AlienBullet(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('light green')
        self.penup()
        self.goto(cor)
        self.setheading(270)
        self.speed(1)

    def move(self):
        self.forward(10)

    def remove(self):
        self.hideturtle()


class AlienBullets():
    def __init__(self):
        self.alien_bullets_list = []

    # Create alien bullet
    def create_alien_bullet(self, alien_cor):
        self.alien_bullets_list.append(AlienBullet(cor=alien_cor))

    # Remove alien bullet once it hits other objects or out of the frame
    def remove_bullet(self, bullet):
        index = self.alien_bullets_list.index(bullet)
        self.alien_bullets_list[index].remove()
        self.alien_bullets_list.remove(bullet)

    # Reset(Remove) all the alien bullets from list when the ship is hit.
    def reset_alien_bullet(self):
        for bullet in self.alien_bullets_list:
            bullet.remove()
        self.alien_bullets_list = []
