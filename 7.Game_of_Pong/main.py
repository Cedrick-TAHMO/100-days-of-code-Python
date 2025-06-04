#!/usr/bin/env python3
"""
Pong Game Main Module
A classic two-player Pong game implementation using Python's turtle graphics.
"""

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
INITIAL_GAME_SPEED = 0.1
SPEED_INCREMENT = 0.01
PADDLE_DISTANCE = 350
COLLISION_DISTANCE = 50
BOUNDARY_Y = 280
BOUNDARY_X = 380

def setup_screen():
    """Initialize and configure the game screen."""
    screen = Screen()
    screen.title("Game of Pong")
    screen.bgcolor(0, 0, 0)
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    return screen

def setup_game_objects():
    """Initialize all game objects."""
    paddle_right = Paddle(PADDLE_DISTANCE, 0, "pink")
    paddle_left = Paddle(-PADDLE_DISTANCE, 0, "green")
    ball = Ball()
    scoreboard = Scoreboard()
    return paddle_right, paddle_left, ball, scoreboard

def setup_controls(screen, paddle_right, paddle_left):
    """Configure game controls for both players."""
    screen.listen()
    # Right paddle controls (Arrow keys)
    screen.onkey(paddle_right.up, "p")
    screen.onkey(paddle_right.down, "l")
    # Left paddle controls (W/S keys)
    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")

def reset_round(ball, paddle_right, paddle_left):
    """Reset the game state for a new round."""
    ball.center_ball()
    paddle_right.center_paddle()
    paddle_left.center_paddle()

def main():
    """Main game loop and initialization."""
    screen = setup_screen()
    paddle_right, paddle_left, ball, scoreboard = setup_game_objects()
    setup_controls(screen, paddle_right, paddle_left)
    
    game_speed = INITIAL_GAME_SPEED
    game_is_on = True

    while game_is_on:
        time.sleep(game_speed)
        screen.update()
        ball.move()

        # Wall collision detection
        if abs(ball.ycor()) > BOUNDARY_Y:
            ball.bounce_y()

        # Paddle collision detection
        if ((ball.distance(paddle_right) < COLLISION_DISTANCE and ball.xcor() > 340) or
            (ball.distance(paddle_left) < COLLISION_DISTANCE and ball.xcor() < -340)):
            ball.bounce_x()
            game_speed = max(game_speed - SPEED_INCREMENT, 0.01)

        # Score handling - right paddle misses
        if ball.xcor() > BOUNDARY_X:
            reset_round(ball, paddle_right, paddle_left)
            scoreboard.l_point()
            game_speed = INITIAL_GAME_SPEED

        # Score handling - left paddle misses
        if ball.xcor() < -BOUNDARY_X:
            reset_round(ball, paddle_right, paddle_left)
            scoreboard.r_point()
            game_speed = INITIAL_GAME_SPEED

    screen.exitonclick()

if __name__ == "__main__":
    main()