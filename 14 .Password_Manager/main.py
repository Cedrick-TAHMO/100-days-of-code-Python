# --------------------------- CONSTANTS & IMPORTS ---------------------------
from tkinter import *
import pandas as pd
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# --------------------------- PASSWORD GENERATOR ---------------------------
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    symbol_letters = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_letters = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pw_letters + symbol_letters + numbers_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# --------------------------- SAVE PASSWORD ---------------------------
# Using Pandas to insert input from form
def save_pw():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error 404:", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                      f"\nEmail: {email} \nPassword: {password} \nIs it ok to save")
        if is_ok:
            df = pd.DataFrame([[f"{website} | {email} | {password}"]])
            df.to_csv("data.txt", mode="a", index=False, header=False)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    website_entry.focus()
# --------------------------- UI SETUP ---------------------------

# Configure the main window
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")  # Add padding and set background color

# Create and configure the logo canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=FALSE)
logo_img = PhotoImage(file="logo.png")  # Load the logo image
canvas.create_image(100, 100, image=logo_img)  # Center the image in canvas
canvas.grid(row=0, column=1)

# Website input section
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")  # Span across 2 columns, align left
website_entry.focus()

# Email/Username input section
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")  # Span across 2 columns, align left
email_entry.insert(0, "johndoe@gmail.com")

# Password input section
password_label = Label(text="Password", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w")  # Align left

# Password generation button
generate_pw_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_pw_button.grid(column=2, row=3, sticky="w")  # Align left

# Add Button
add_button = Button(text="Add", width=42, command=save_pw)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

# Start the application main loop
window.mainloop()