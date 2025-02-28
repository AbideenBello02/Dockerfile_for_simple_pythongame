from turtle import Turtle

ROAD_POSITION = [(-290, 0), (-290, 150), (-290, -150)]


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.create_road()

    def create_road(self):
        for position in ROAD_POSITION:
            new_road = Turtle()
            new_road.penup()
            new_road.goto(position)
            new_road.pendown()
            new_road.goto(310, new_road.ycor())
