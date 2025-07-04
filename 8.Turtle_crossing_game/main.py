
"""
Turtle Crossing Game
A game where the player needs to cross a busy road while avoiding cars.
"""

import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

def setup_game():
    """Initialize the game screen and objects."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)  # Turn off automatic updates for smooth animation
    return screen

def main():
    # Initialize game components
    screen = setup_game()
    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    # Set up keyboard controls
    screen.listen()
    screen.onkeypress(player.move, "Up")

    # Main game loop
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)  # Control game speed
        screen.update()
        
        # Game mechanics
        car_manager.create_car()
        car_manager.move_cars()

        # Check if player completed the level
        if player.ycor() > 200:
            player.reset_turtle()
            scoreboard.up_the_level()
            car_manager.level_up()

        # Collision detection
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()

if __name__ == "__main__":
    main()