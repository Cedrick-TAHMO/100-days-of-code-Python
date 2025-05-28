# Import required modules
import random
from turtle import Turtle, Screen

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)  # Set window size to 500x400 pixels

# Initialize race control variables
is_race_on = False
# Get user's bet on which turtle will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define turtle colors and starting positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_position = -230  # Starting x position (adjusted to give more race space)
y_position = -100  # Starting y position for first turtle
all_turtles = []

# Create and position all turtles
for i in range(len(colors)):  # Using len(colors) instead of hardcoded 6 for better maintainability
    hold_color = colors[i]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(hold_color)
    new_turtle.penup()  # Lift pen to avoid drawing lines while positioning
    new_turtle.goto(x=x_position, y=y_position)
    y_position += 50  # Space turtles 50 pixels apart vertically
    all_turtles.append(new_turtle)

# Start race only if user made a bet
if user_bet:
    is_race_on = True

# Main race loop
while is_race_on:
    # Move each turtle a random distance
    for turtle in all_turtles:
        # Check if current turtle has crossed finish line (230 pixels from left)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # Announce race results
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break  # Exit the for loop once we have a winner

        # Move turtle forward by random distance between 0 and 10 pixels
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Keep window open until clicked
screen.exitonclick()