"""
Scoreboard Module
Handles the game score display and management.
"""

from turtle import Turtle

class Scoreboard(Turtle):
    """
    Scoreboard class for displaying and managing game scores.
    Inherits from the Turtle class for graphics rendering.
    """

    FONT_SETTINGS = ("Roboto", 40, "normal")
    SCORE_Y_POSITION = 200

    def __init__(self):
        """Initialize a new scoreboard with default settings."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and redraw the scoreboard with current scores."""
        self.clear()
        # Draw left player score
        self.goto(-100, self.SCORE_Y_POSITION)
        self.write(self.l_score, align='center', font=self.FONT_SETTINGS)
        # Draw right player score
        self.goto(100, self.SCORE_Y_POSITION)
        self.write(self.r_score, align='center', font=self.FONT_SETTINGS)

    def l_point(self):
        """Increment left player's score and update display."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increment right player's score and update display."""
        self.r_score += 1
        self.update_scoreboard()