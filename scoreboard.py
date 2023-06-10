from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-275, 260)
        self.write(f"Level = {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.color("red")
        self.write("Game Over. ", align="center", font=FONT)
