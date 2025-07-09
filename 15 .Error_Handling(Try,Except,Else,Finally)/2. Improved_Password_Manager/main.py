# --------------------------- CONSTANTS & IMPORTS ---------------------------
# Required imports for GUI, message boxes, and random password generation
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip  # For copying text to clipboard
import json

# --------------------------- PASSWORD GENERATOR ---------------------------
def generate_password():
    """
    Generates a secure random password containing letters, numbers, and symbols.
    The password is automatically copied to clipboard and inserted into password entry field.
    """
    password_entry.delete(0, END)
    # Character sets for password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random characters using list comprehension
    pw_letters = [choice(letters) for _ in range(randint(8, 10))]      # 8-10 letters
    symbol_letters = [choice(symbols) for _ in range(randint(2, 4))]    # 2-4 symbols
    numbers_letters = [choice(numbers) for _ in range(randint(2, 4))]   # 2-4 numbers

    # Combine and shuffle all characters
    password_list = pw_letters + symbol_letters + numbers_letters
    shuffle(password_list)

    # Create final password and insert into entry field
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy to clipboard for convenience

# --------------------------- SAVE PASSWORD ---------------------------
def save_pw():
    """
    Saves website, email, and password information to a JSON file.
    Performs validation and handles file operations with error checking.
    """
    # Get data from entry fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Validate input fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error 404:", message="Please don't leave any fields empty!")
    else:
        try:
            # Try to read existing data
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except JSONDecodeError:
            # If file is empty or corrupted, create new data file
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update existing data with new entry
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Clear entry fields and reset focus
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

    ############################
    # JSON Key operation
    #   Write: json.dump()
    #   Read: json.load()
    #   Update: json.update()
    ############################

def search():
    """
    Searches for saved website credentials in the JSON file.
    Displays results in a message box or shows appropriate error messages.
    """
    website = website_entry.get()
    if len(website) != 0:
        try:
            # Attempt to read data file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except JSONDecodeError:
            messagebox.showerror(title='Error 202', message="No Data File Found.")
        else:
            # Check if website exists in saved data
            if website in data:
                search_email = data[website]["email"]
                search_password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {search_email}\nPassword: {search_password}")
            else:
                messagebox.showerror(title="Error 806",
                                   message=f"The website entered: {website}, does not exist")
    else:
        messagebox.showerror(title='Error 560', message="Please enter a Website")

# --------------------------- UI SETUP ---------------------------
# Main window configuration
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

# Logo setup
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=FALSE)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website section UI elements
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

# Search button
search_button = Button(text="Search", bg="blue", width=14, command=search)
search_button.grid(column=2, row=1, sticky="w")

# Email/Username section UI elements
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "johndoe@gmail.com")

# Password section UI elements
password_label = Label(text="Password", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

# Password generation and Add buttons
generate_pw_button = Button(text="Generate Password", bg="white", command=generate_password, width=14)
generate_pw_button.grid(column=2, row=3, sticky="w")
add_button = Button(text="Add", width=42, command=save_pw)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

# Start application
window.mainloop()