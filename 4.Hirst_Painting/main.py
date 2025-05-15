import random
from turtle import Turtle, Screen

# --- Configuration Constants ---
PAINTING_SIZE = 10     # Number of dots per row/column
SPACING = 50           # Space between dots
DOT_SIZE = 20          # Size of each dot

# --- Color Palette (RGB) ---
color_list = [
    (110, 180, 224), (6, 178, 214), (239, 142, 62), (28, 91, 163), (23, 196, 101),
    (215, 125, 185), (238, 207, 3), (209, 169, 5), (239, 62, 138), (195, 8, 75),
    (242, 60, 39), (235, 211, 81), (224, 164, 216), (27, 49, 142), (186, 39, 128),
    (144, 228, 208), (105, 102, 191), (251, 173, 142), (82, 205, 158), (207, 66, 21),
    (144, 208, 221), (3, 61, 52), (7, 137, 95), (78, 35, 39), (144, 38, 34),
    (174, 184, 230), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0),
    (128, 0, 128), (255, 192, 203), (46, 139, 87), (70, 130, 180), (220, 20, 60),
    (0, 128, 128), (139, 69, 19), (255, 215, 0), (148, 0, 211), (34, 139, 34),
    (210, 105, 30), (123, 104, 238), (233, 150, 122), (72, 61, 139), (178, 34, 34)
]

# --- Initialize Turtle ---
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.showturtle()  # Optional: show turtle while painting

# --- Dot Painting Generation ---
def draw_dot_painting():
    """Draws a grid of randomly colored dots using turtle graphics."""
    y_gap = -200  # Starting y-coordinate

    for row in range(PAINTING_SIZE):
        x_gap = 0  # Reset x-coordinate at the start of each row

        for col in range(PAINTING_SIZE + 1):
            # Choose a random RGB color and convert to 0–1 range
            rgb = tuple(c / 255 for c in random.choice(color_list))
            tim.goto(x_gap, y_gap)
            tim.dot(DOT_SIZE, rgb)
            x_gap += SPACING

        y_gap += SPACING

# --- Run Drawing ---
draw_dot_painting()

# --- Setup Screen ---
screen = Screen()
screen.exitonclick()  # Close the window on click
