from turtle import Screen
import turtle
import pandas

from data import Data

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data_set = Data()


right_ans_count = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f'{len(data_set.found)}/50Guess the State',
                                    prompt="What's another state's name")
    print(answer_state)


    #Check if the user's input is correct
    if answer_state == 'exit':
        missed_states = [state for state in data_set.states if state not in data_set.found]

        states_left = pandas.DataFrame(data=missed_states,
                                       columns=['Missed States']).to_csv("missed_states.csv",
                                                                         index=True)


        print("\nYou've exited the game.")
        print(f"fYou guessed {len(data_set.found)} out of {len(data_set.states)} states.")
        print("States you missed:")
        for state in missed_states:
            print("-", state)
        game_is_on = False

    elif data_set.has_state(answer_state):
        print(f"Correct! {len(data_set.found)} out of {len(data_set.states)}")
    else:
        print("Already guessed or not valid state.")

    if data_set.all_states_found():
        print("Congratulations! You've found all the states!!")
        game_is_on = False
turtle.mainloop()