import pandas as pd
from turtle import Turtle

class Data(Turtle):

    def __init__(self):
        df = pd.read_csv("50_states.csv")
        self.states = df['state'].unique().tolist()
        self.x_cor = df['x'].tolist()
        self.y_cor = df['y'].tolist()
        super().__init__()
        self.hideturtle()
        self.penup()
        self.count = 0
        self.found = []

    def found_state(self, answer_state):
        self.color('black')
        index = self.states.index(answer_state)
        self.goto(self.x_cor[index], self.y_cor[index])
        self.write(arg=f'{answer_state}', align="center", move=False, font=("Courier", 10, "normal"))

    def has_state(self, user_state):
        user_state = user_state.title() # Normalize input

        if user_state in self.states and user_state not in self.found:
            self.found.append(user_state)
            self.found_state(user_state)
            return True
        else:
            return False

    def all_states_found(self):
        return len(self.found) == len(self.states)