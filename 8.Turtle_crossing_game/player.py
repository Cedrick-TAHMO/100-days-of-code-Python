"""
Player Module
Handles the player turtle's movement and position management.
"""

from turtle import Turtle

# Constants
STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    """
    Player class representing the turtle that the user controls.
    Inherits from Turtle class.
    """
    
    def __init__(self):
        """Initialize the player turtle with starting position and appearance."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)  # Face upward
        self.goto(STARTING_POSITION)

    def move(self):
        """Move the turtle forward by the defined distance."""
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        """Reset the turtle to its starting position."""
        self.goto(STARTING_POSITION)