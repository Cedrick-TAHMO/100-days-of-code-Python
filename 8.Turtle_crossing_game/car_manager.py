"""
Car Manager Module
Handles the creation and movement of cars in the game.
"""

import random
from turtle import Turtle

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    Manages the creation and movement of cars across the screen.
    """
    
    def __init__(self):
        """Initialize the car manager with empty car list and starting speed."""
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Create a new car with random properties.
        Cars are created with a 1/6 probability each time this method is called.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-200, 200)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars from right to left across the screen."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase the speed of cars when player completes a level."""
        self.car_speed += MOVE_INCREMENT