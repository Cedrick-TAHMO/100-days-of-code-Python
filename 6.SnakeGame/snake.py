"""
Snake Module
Handles the snake's behavior, movement, and growth mechanics.
"""

from turtle import Turtle

# Snake Configuration
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    """
    A class to represent the snake in the game.
    
    Attributes:
        segments (list): List of turtle objects forming the snake's body
        head (Turtle): The first segment of the snake (its head)
    """
    
    def __init__(self):
        """Initialize the snake with its starting segments."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake body."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Add a new segment to the snake's body.
        
        Args:
            position (tuple): The (x, y) coordinates for the new segment
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the snake when it eats food."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by updating each segment's position."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change snake's direction to upward if not moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change snake's direction to downward if not moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Change snake's direction to right if not moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Change snake's direction to left if not moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)