import turtle as t
import random

COLOR = ["red", "yellow", "blue", "black", "gray", "green"]


class Car:

    def __init__(self):
        self.kars = []
        self.car_start_speed = 5



    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = t.Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLOR))
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-220, 220)
            car.goto(300, random_y)
            self.kars.append(car)

    def car_move(self):
        for x in self.kars:
            x.back(self.car_start_speed)

    def up_the_speed(self):
        self.car_start_speed += 10

