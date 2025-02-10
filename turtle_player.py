from turtle import Turtle

class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark olive green")
        self.penup()
        self.setheading(90)
        self.set_turtle()

    def set_turtle(self):
        """Moves the turtle to the starting position"""
        self.goto(x=0, y=-280)

    def move_up(self):
        """The turtles moves up by 10 pixels"""
        self.forward(10)

    def move_down(self):
        """The turtle moves down by 10 pixels"""
        self.backward(10)