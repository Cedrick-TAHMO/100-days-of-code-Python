"""
Paddle Module
Handles the creation and movement of game paddles.
"""

from turtle import Turtle

class Paddle(Turtle):
    """
    Paddle class representing a player's paddle in the game.
    Inherits from the Turtle class for graphics rendering.
    """

    MOVE_DISTANCE = 20  # Constant for paddle movement distance
    PADDLE_WIDTH = 1
    PADDLE_HEIGHT = 6

    def __init__(self, x_pos, y_pos):
        """
        Initialize a new paddle.
        
        Args:
            x_pos (int): Initial x-coordinate position
            y_pos (int): Initial y-coordinate position
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=self.PADDLE_HEIGHT, stretch_len=self.PADDLE_WIDTH)
        self.penup()
        self.initial_x = x_pos
        self.initial_y = y_pos
        self.goto(x_pos, y_pos)

    def up(self):
        """Move the paddle upward."""
        new_y = self.ycor() + self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        """Move the paddle downward."""
        new_y = self.ycor() - self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def center_paddle(self):
        """Reset the paddle to its initial position."""
        self.goto(self.initial_x, self.initial_y)