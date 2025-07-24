#!/usr/bin/env python3
"""
Canadian Province Game
A educational game to help learn Canadian provinces through an interactive map
"""

from turtle import Screen
import turtle
import pandas
from data import Data  # Add this import

# Set up the game window
screen = Screen()
screen.title("Canadian Province Game")
image = "blank_canadian_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

# Initialize the data manager
data_set = Data()

game_is_on = True

while game_is_on:
    # Get user input with current progress display
    answer_province = screen.textinput(
        title=f'{len(data_set.found)}/13 Guess the Province',
        prompt="What's another province's name: "
    )

    # Handle game exit
    if answer_province == 'exit':
        # Create list of missed provinces
        missed_provinces = [province for province in data_set.states 
                          if province not in data_set.found]

        # Save missed provinces to CSV file
        province_left = pandas.DataFrame(
            data=missed_provinces,
            columns=["Missed States"]
        ).to_csv("missed_provinces.csv", index=True)

        # Display game results
        print("\nYou've exited the game.")
        print(f"You guessed {len(data_set.found)} out of {len(data_set.states)} provinces.")
        print("Provinces you missed:")
        for province in missed_provinces:
            print("-", province)
        game_is_on = False

    # Handle correct guess
    elif data_set.has_state(answer_province):
        print(f"Correct! {len(data_set.found)} out of {len(data_set.states)}.")
    # Handle incorrect guess
    else:
        print("Already guessed or not a valid province.")

    # Check for game completion
    if data_set.all_states_found():
        print("Congratulation! You've found all the state!!")
        game_is_on = False

# Keep the window open until manually closed
screen.mainloop()