"""
Scoreboard Module
Handles the game's scoring system and display.
"""

from turtle import Turtle

# Scoreboard Configuration
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCORE_POSITION = (0, 200)
GAME_OVER_POSITION = (0, 0)

class Scoreboard(Turtle):
    """
    A class to handle and display the game's score.
    
    Inherits from:
        Turtle: Base turtle graphics class
    """

    def __init__(self):
        """Initialize the scoreboard with a starting score and display settings."""
        super().__init__()
        with open("data.txt") as f: # New Improvement
            data = f.read() #
        self.score = 0
        self.high_score = int(data)
        self.color("violet")
        self.hideturtle()
        self.penup()
        self.score_display()


    def score_display(self):
        """Update and display the current score."""
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            score = self.score
            with open("data.txt", mode='w') as f:
                f.write(str(self.score))
        self.score = 0
        self.score_display()
    # def score_game_over(self):
    #     """Display the game over message and final score."""
    #     self.clear()
    #     self.goto(GAME_OVER_POSITION)
    #     self.write(f'Game Over\nFinal Score: {self.score}',
    #               False, ALIGNMENT, FONT)

    def add_score(self):
        """Increment the score by one point."""
        self.score += 1