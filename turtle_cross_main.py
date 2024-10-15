#TODO-1 : Layar (600x600)px
import random
from turtle import Screen
from turtle_crossing import Go_Turtle
from car import Car
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
#TODO-2 : Set tracer(0)
screen.tracer(0)
#TODO-1 : set time sleep 0.1
#TODO-1 : While loop buat mobil terus generate
jack = Go_Turtle()
car = Car()
score = Score()



screen.onkey(fun=jack.move, key="Up")

## stop the game on press 'q'abs
def quit_game():
    screen.bye()

screen.onkey(fun=quit_game, key='q')

game_on = True
diff = 0.1
while game_on:
    time.sleep(diff)
    car.create_car()
    car.car_move()
    for x in car.kars:
        if x.distance(jack) < 25:
            score.game_over()
            game_on = False
    if jack.at_finish():
        # diff /= 10
        car.up_the_speed()
        score.update()







    screen.update()












screen.exitonclick()