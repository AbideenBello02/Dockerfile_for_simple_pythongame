
import time
from turtle import Screen

from cars import CarManager
from player import Player
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Road crosser")
screen.tracer(0)


boy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
road = Road()

screen.listen()
screen.onkey(boy.player_move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_down_cars()
    car_manager.move_up_cars()

    for car in car_manager.up_cars:
        if car.distance(boy) < 20:
            game_is_on = False
            scoreboard.game_over()

    for car in car_manager.down_cars:
        if car.distance(boy) < 20:
            game_is_on = False
            scoreboard.game_over()

    if boy.ycor() > 155:
        boy.go_to_start()
        car_manager.level_up()
        scoreboard.increment_score()

screen.exitonclick()



"THIS IS TO TEST JENKINS BUILD PIPELINE"
"New line updated"