# ------------------------------------ IMPORTS ------------------------------------
import random
from tkinter import *
from tkinter import messagebox
import pandas as pd

# ---------------------------------- CONSTANTS -------------------------------------
# UI Constants
BACKGROUND_COLOR = "#B1DDC6"  # Light green background color
CARD_WIDTH = 800              # Width of flashcard in pixels
CARD_HEIGHT = 526             # Height of flashcard in pixels

# --------------------------------- VARIABLES -------------------------------------
to_learn = {}                 # Dictionary to store words that need to be learned
current_card = {}             # Current card being displayed

# -------------------------- DATA INITIALIZATION ---------------------------------
# Try to load the user's progress file first
try:
    df = pd.read_csv('data/words_to_learn.csv')  # Load saved learning progress
except FileNotFoundError:
    # If no progress file exists, load the original word list
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")  # Convert DataFrame to list of dictionaries
else:
    # If progress file exists, use it for continued learning
    to_learn = df.to_dict(orient="records")  # Convert DataFrame to list of dictionaries


# --------------------------- WORD MANAGEMENT -----------------------------
def word_generator():
    """
    Generates a new random flashcard from the words to learn.
    - Cancels any existing flip timer
    - Selects a random word from the to_learn dictionary
    - Configures the card to show the French word
    - Sets a 3-second timer to flip the card
    """
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel previous timer to prevent multiple flips
    current_card = random.choice(to_learn)  # Select a random word pair

    # Configure the front of the card (French side)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_img, image=card_front)

    # Set timer to flip card after 3 seconds
    flip_timer = window.after(ms=3000, func=flip_card)

def flip_card():
    """
    Flips the card to show the English translation.
    - Changes the card image to the back side
    - Updates the title to 'English'
    - Shows the English translation of the current word
    - Changes text color to white for better visibility on dark background
    """
    canvas.itemconfig(card_title, text="English", fill='white')  # Change title and color
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')  # Show English translation
    canvas.itemconfig(card_img, image=card_back)  # Change to card back image

def already_know():
    """
    Handles when user indicates they know the current word.
    - Removes the current card from the to_learn list
    - Generates a new random word
    - Saves the updated to_learn list to CSV file
    This allows for tracking progress across sessions.
    """
    to_learn.remove(current_card)  # Remove word from learning list
    word_generator()  # Show a new word

    # Save progress to CSV file for future sessions
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
# --------------------------- UI SETUP -------------------------------
# Main window configuration
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=flip_card)

# Card design
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT,background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(CARD_WIDTH//2,CARD_HEIGHT//2,image=card_front)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Title")
card_word = canvas.create_text(400, 263, font=("Ariel", 40, "bold"), text="word")
canvas.grid(row=0, column=0, columnspan=2)

# Reject button
reject_img = PhotoImage(file="images/wrong.png")
reject_btn = Button(image=reject_img, highlightthickness=0, command=word_generator)
reject_btn.grid(row=1, column=0)

# Valid button
valid_img = PhotoImage(file="images/right.png")
valid_btn = Button(image=valid_img, highlightthickness=0, command=already_know)
valid_btn.grid(row=1, column=1)

word_generator()

window.mainloop()



