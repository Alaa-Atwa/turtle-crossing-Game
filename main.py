import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating the turtle and listening to key presses.
player = Player()
screen.listen()
screen.onkey(player.move_up, 'Up')

car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # randomly creating a car every a while.
    chance = random.randint(0, 5)
    if chance == 1:
        car_manager.create_car()

    car_manager.move_cars()

    # detect crashing with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # reset player to the starting position when reaching end of level
    if player.finished_level():
        player.goto(0, -280)
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()  # prevent screen from closing on its own.
