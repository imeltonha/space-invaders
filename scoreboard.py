from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.lives = 3
        self.scores = 0

        self.penup()
        self.hideturtle()
        self.color("white")

        self.goto((-480, -470))
        self.write(f"Life: {self.lives}", align="right", font=("Ariel", 20, "bold"))

        self.goto((-250, -470))
        self.write(f"Score: {self.scores}", align="right", font=("Ariel", 20, "bold"))

    # Update lives once the ship is hit
    def update_lives(self):
        self.clear()
        self.goto((-480, -470))
        self.write(f"Life: {self.lives}", align="right", font=("Ariel", 20, "bold"))

        self.goto((-250, -470))
        self.write(f"Score: {self.scores}", align="right", font=("Ariel", 20, "bold"))

    # Update scores function once the alien ship is hit
    def update_scores(self):
        self.clear()
        self.goto((-480, -470))
        self.write(f"Life: {self.lives}", align="right", font=("Ariel", 20, "bold"))

        self.goto((-250, -470))
        self.write(f"Score: {self.scores}", align="right", font=("Ariel", 20, "bold"))

    # Show game over when the lives run out
    def game_over(self):
        self.goto((0, 0))
        self.color("red")
        self.write("Game Over!", align="center", font=("Ariel", 60, "bold"))
        # self.write(f"Life: {self.lives}", align="right", font=("Ariel", 20, "bold"))


class SeparateLine(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((-550, -430))
        self.pendown()
        self.goto((550, -430))
        self.penup()
