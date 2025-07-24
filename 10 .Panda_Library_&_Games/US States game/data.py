import pandas as pd
from turtle import Turtle

class Data(Turtle):
    """A class that manages US states data and their visualization using Turtle graphics"""

    def __init__(self):
        # Read the CSV file containing state data
        df = pd.read_csv("50_states.csv")
        # Extract unique state names and coordinates into lists
        self.states = df['state'].unique().tolist()
        self.x_cor = df['x'].tolist()
        self.y_cor = df['y'].tolist()
        
        # Initialize the Turtle parent class
        super().__init__()
        # Hide the turtle cursor and lift the pen
        self.hideturtle()
        self.penup()
        
        # Initialize counter and list to track found states
        self.count = 0
        self.found = []

    def found_state(self, answer_state):
        """
        Write the state name at its corresponding coordinates on the map
        
        Args:
            answer_state (str): Name of the state to be displayed
        """
        self.color('black')
        # Get the index of the state to find its coordinates
        index = self.states.index(answer_state)
        # Move to the state's coordinates
        self.goto(self.x_cor[index], self.y_cor[index])
        # Write the state name with specified formatting
        self.write(arg=f'{answer_state}', align="center", move=False, font=("Courier", 10, "normal"))

    def has_state(self, user_state):
        """
        Check if the given state exists and hasn't been found yet
        
        Args:
            user_state (str): State name provided by the user
            
        Returns:
            bool: True if state exists and hasn't been found, False otherwise
        """
        # Capitalize first letter of each word in state name
        user_state = user_state.title()

        # Check if state exists and hasn't been found yet
        if user_state in self.states and user_state not in self.found:
            self.found.append(user_state)
            self.found_state(user_state)
            return True
        else:
            return False

    def all_states_found(self):
        """
        Check if all states have been found
        
        Returns:
            bool: True if all states have been found, False otherwise
        """
        return len(self.found) == len(self.states)