FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.level = 0
        self.write(f"Level: {self.level}", False, align="left", font=FONT)



    def update_level(self):
        self.clear()
        self.level += 1
        self.hideturtle()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, align="center", font=FONT)


