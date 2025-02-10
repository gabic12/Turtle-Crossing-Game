from turtle import Screen
from turtle_player import TurtlePlayer
from cars import Cars
from scoreboard import Scoreboard
import time

#Setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Setting the game variables
game_on = True
turtle_player = TurtlePlayer()
scoreboard = Scoreboard()
cars = Cars()

#Screen will listen for key inputs
screen.listen()
screen.onkey(fun=turtle_player.move_up, key="Up")
screen.onkey(fun=turtle_player.move_down, key="Down")

while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    #Collision with a car
    for car in cars.car_list:
        if car.distance(turtle_player) < 20:
            scoreboard.game_over()
            game_on = False

    #Turtle has reached the finish line
    if turtle_player.ycor() > 280: #280 is the Y cord of the finish line
        scoreboard.level_up()
        turtle_player.set_turtle()
        cars.car_speed += 10 #Car speed is increased with each completed level

screen.exitonclick()