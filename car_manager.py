from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        #  width = 1 * 20 , len = 2 * 20
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        xcor = 310
        ycor = random.randrange(-230, 230)
        new_car.goto(xcor, ycor)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

