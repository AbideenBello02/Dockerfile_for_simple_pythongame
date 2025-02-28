from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
DOWN_CARS_POSITION = [-25, -75, -125]
UP_CARS_POSITION = [25, 75, 125]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.down_cars = []
        self.up_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_create = random.randint(1, 10)
        if random_create == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=0.6, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(DOWN_CARS_POSITION)
            new_car.goto(300, random_y)
            self.down_cars.append(new_car)

        elif random_create == 2:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=0.6, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(UP_CARS_POSITION)
            new_car.goto(-300, random_y)
            self.up_cars.append(new_car)

    def move_down_cars(self):
        for cars in self.down_cars:
            cars.backward(self.car_speed)

    def move_up_cars(self):
        for cars in self.up_cars:
            cars.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
