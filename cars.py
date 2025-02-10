from turtle import Turtle
import random

COLORS_LIST = ["red", "orange", "yellow", "green", "blue", "purple"]

class Cars:

    def __init__(self):
        self.car_list = []
        self.car_speed = 0 #With each completed level, the speed will increase by 10

    def create_car(self):
        """Creates random cars and places them on the left side of the screen"""
        random_chance = random.randint(1, 6) #Only 1 in 6 times a car will be created
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS_LIST))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.car_list.append(new_car)

    def move_cars(self):
        """Moves the cars, speed increases with each completed level"""
        for car in self.car_list:
            car.backward(5 + self.car_speed)