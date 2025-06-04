"""
Scoreboard Module
Handles the game's scoring system and display of game status.
"""

from turtle import Turtle

# Constants
FONT = ("Courier", 24, "normal")
X_POSITION = -200
Y_POSITION = 200

class Scoreboard(Turtle):
    """
    Manages and displays the game score and status messages.
    Inherits from Turtle class.
    """
    
    def __init__(self):
        """Initialize the scoreboard with starting level and position."""
        super().__init__()
        self.game_level = 0
        self.hideturtle()
        self.penup()
        self.goto(X_POSITION, Y_POSITION)
        self.up_the_level()

    def up_the_level(self):
        """Update and display the current game level."""
        self.clear()
        self.game_level += 1
        self.write(
            arg=f'Level {self.game_level}',
            move=False,
            align="left",
            font=FONT
        )
        self.color("black")

    def game_over(self):
        """Display the game over message in the center of the screen."""
        game_over_turtle = Turtle()
        game_over_turtle.hideturtle()
        game_over_turtle.color("black")
        game_over_turtle.penup()
        game_over_turtle.write(
            arg='Game Over',
            move=False,
            align="center",
            font=FONT
        )