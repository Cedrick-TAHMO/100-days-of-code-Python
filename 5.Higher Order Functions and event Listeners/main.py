from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_right():
    tim.right(90)
    tim.forward(10)

def move_left():
    tim.left(90)
    tim.forward(10)

screen.listen()
screen.onkey(move_forwards, "space")
screen.onkey(move_left, "Left")
screen.onkey(move_backwards, "v")
screen.onkey(move_right, "Right")
screen.exitonclick()