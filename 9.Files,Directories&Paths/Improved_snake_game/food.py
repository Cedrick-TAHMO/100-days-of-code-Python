"""
Food Module
Handles the creation and placement of food items in the game.
"""

import random
from turtle import Turtle

class Food(Turtle):
    """
    A class to represent the food in the game.
    
    Inherits from:
        Turtle: Base turtle graphics class
    """
    
    def __init__(self):
        """Initialize the food with specific appearance settings."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random position on the screen."""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)