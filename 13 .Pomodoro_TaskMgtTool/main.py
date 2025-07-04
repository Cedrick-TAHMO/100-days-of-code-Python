"""
Pomodoro Timer Application
A productivity tool implementing the Pomodoro Technique with work and break intervals
"""

import math
import tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Color scheme constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Timer duration constants (in minutes)
WORK_MIN = 25           # Standard Pomodoro work session
SHORT_BREAK_MIN = 5     # Short break duration
LONG_BREAK_MIN = 20     # Long break duration

# Global variables for tracking timer state
REPS = 0               # Counts the number of work/break cycles
CHECK_COUNT = 1        # Tracks completed work sessions
TIMER = None           # Stores the timer object

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reset all timer components to initial state."""
    global REPS, CHECK_COUNT
    window.after_cancel(TIMER)    # Cancel any running timer
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    REPS = 0
    CHECK_COUNT = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Start the Pomodoro timer sequence."""
    global REPS, CHECK_COUNT
    REPS += 1

    # Convert all times to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine which timer to start based on REPS
    if REPS % 8 == 0:
        # Every 8th rep is a long break
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED, bg=YELLOW)
    elif REPS % 2 == 0:
        # Even reps are short breaks
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        # Odd reps are work sessions
        count_down(work_sec)
        title_label.config(text="Time to Grind!!", fg=GREEN, bg=YELLOW)
        check_mark.config(text="✓"*CHECK_COUNT)
        CHECK_COUNT += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Implement the countdown timer functionality.
    
    Args:
        count (int): Time remaining in seconds
    """
    # Convert seconds to minutes and seconds format
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    # Update timer display with formatted time
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    
    if count > 0:
        global TIMER
        TIMER = window.after(10, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# Main window configuration
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label at the top
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

# Canvas setup for tomato image and timer display
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=FALSE)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Control buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)

# Checkmark indicator for completed sessions
check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=1)

# Start the application
window.mainloop()