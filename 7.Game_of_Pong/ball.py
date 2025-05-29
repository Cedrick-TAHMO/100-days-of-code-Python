"""
Ball Module
Handles the creation and movement of the game ball.
"""

from turtle import Turtle

class Ball(Turtle):
    """
    Ball class representing the game ball.
    Inherits from the Turtle class for graphics rendering.
    """

    def __init__(self):
        """Initialize a new ball with default settings."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Move the ball based on its current direction."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the vertical direction of the ball."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the horizontal direction of the ball."""
        self.x_move *= -1

    def center_ball(self):
        """Reset the ball to center position and reverse direction."""
        self.goto(0, 0)
        self.bounce_x()