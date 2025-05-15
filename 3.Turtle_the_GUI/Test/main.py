import random
import turtle
from turtle import *

## Timmy the turtle
timmy = Turtle()
timmy.shape("turtle")

# Method 1: Using random RGB values
def random_color():
    r = random.random()  # Random float between 0 and 1
    g = random.random()
    b = random.random()
    return (r, g, b)

# Method 2: Using predefined color names
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink",
          "brown", "gray", "cyan", "magenta", "violet"]
directions = [0, 90, 180, 270]
timmy.filling()
timmy.speed(20)


# Turtle will not draw a Spirograph
while True:
    timmy.color(random.choice(colors))
    timmy.circle(100)
    timmy.left(5)
    current_angle = timmy.heading()
    print(current_angle)
    if current_angle == 0:
        break

# # Draw a Random Walk
# timmy.pensize(10)
# timmy.shapesize(1)
# for _ in range(300):
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# # Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# angle = 360
# step = 100
# sides = 3
# for i in range(8):
#     timmy.color(random_color())
#     while True:
#
#         fangle = angle / sides
#         timmy.forward(step)
#         timmy.right(fangle)
#         if abs(timmy.pos())<1:
#             timmy.color()
#             sides += 1
#             break



# ## Use Timmy to draw a square
# for i in range(4):
#     timmy.left(90)
#     timmy.forward(100)
#
# ## Use timmy to draw dotted lines
# for i in range(50):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


## Draw a star
# timmy.color('red', 'yellow')
# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(100)
#     if abs(timmy.pos()) < 1:
#         break
# timmy.end_fill()
# done()





screen = Screen()
screen.exitonclick()