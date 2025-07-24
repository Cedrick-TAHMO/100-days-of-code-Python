#!/usr/bin/env python3
"""
Canadian Provinces Game Data Module
Handles the data management and visualization of provinces on the map
"""

from turtle import Turtle
import pandas as pd

class Data(Turtle):
    """
    A class that manages Canadian provinces data and their visualization
    Inherits from Turtle for drawing capabilities
    """

    def __init__(self):
        """Initialize the Data object with provinces information and setup"""
        super().__init__()
        # Load provinces data from CSV file
        df = pd.read_csv("10_provinces.csv")
        # Extract provinces names and coordinates
        self.province = df['province'].unique().tolist()
        self.x_cor = df['x'].tolist()
        self.y_cor = df['y'].tolist()
        # Configure turtle settings
        self.penup()
        self.hideturtle()
        # Initialize game tracking variables
        self.count = 0
        self.found = []

    def found_province(self, user_response):
        """
        Display the province name on the map when correctly guessed
        
        Args:
            user_response (str): The correctly guessed province name
        """
        self.color("black")
        # Find the coordinates for the province
        index = self.province.index(user_response)
        self.goto(self.x_cor[index], self.y_cor[index])
        # Write province name on the map
        self.write(arg=f'{user_response}', align="center", move=False, font=("Courier", 10, "normal"))

    def has_province(self, user_response):
        """
        Check if the guessed province exists and hasn't been found yet
        
        Args:
            user_response (str): The user's guess for a province name
            
        Returns:
            bool: True if province exists and hasn't been found, False otherwise
        """
        user_response = user_response.title()

        if user_response in self.province and user_response not in self.found:
            self.found.append(user_response)
            self.found_province(user_response)
            return True
        else:
            return False

    def all_provinces_found(self):
        """
        Check if all provinces have been discovered
        
        Returns:
            bool: True if all provinces found, False otherwise
        """
        return len(self.found) == len(self.province)