#!/usr/bin/env python3
"""
Snake Game Main Module
This is the main entry point for the Snake Game. It handles the game loop,
collision detection, and user input processing.

"""

from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

# Game Configuration
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_SPEED = 0.2
COLLISION_DISTANCE_FOOD = 15
COLLISION_DISTANCE_WALL = 280
COLLISION_DISTANCE_TAIL = 10

def setup_screen():
    """Initialize and configure the game screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen

def setup_controls(screen, snake):
    """Set up keyboard controls for the snake."""
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

def main():
    """Main game loop and initialization."""
    screen = setup_screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    setup_controls(screen, snake)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(GAME_SPEED)
        snake.move()
        scoreboard.score_display()

        # Food collision detection
        if snake.head.distance(food) < COLLISION_DISTANCE_FOOD:
            food.refresh()
            snake.extend()
            scoreboard.add_score()

        # Wall collision detection
        if (abs(snake.head.xcor()) > COLLISION_DISTANCE_WALL or 
            abs(snake.head.ycor()) > COLLISION_DISTANCE_WALL):
            game_is_on = False
            scoreboard.score_game_over()

        # Tail collision detection
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < COLLISION_DISTANCE_TAIL:
                game_is_on = False
                scoreboard.score_game_over()

    screen.exitonclick()

if __name__ == "__main__":
    main()