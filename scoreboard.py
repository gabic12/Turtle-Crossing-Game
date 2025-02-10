from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.level = 1
        self.update_level()

    def update_level(self):
        """Updates the level"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def level_up(self):
        """Increases the level by 1"""
        self.level += 1
        self.update_level()

    def game_over(self):
        """Display the Game Over message"""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))