# Create a letter using starting_letter.txt for each name in invite_names.txt
#Replace the [name} placeholder with the actual name.
#Save the letters in the folder "ReadyToSend"
import os

# Paths
letter_template_path = "../Mail_merge_Project/Input/Letters/starting_letter.txt"
names_path = "../Mail_merge_Project/Input/Names/invited_names.txt"
output_folder = "../Mail_merge_Project/ReadyToSend"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the template
with open(letter_template_path, "r") as f:
    content = f.read()

# Read names and generate letters
with open(names_path, "r") as file:
    for name in file:
        name = name.strip()  # Remove any whitespace or newlines
        new_letter = content.replace("[Name]", name)

        # Create a unique filename for each letter
        output_path = os.path.join(output_folder, f'letter_for_{name}.txt')

        # Write the personalized letter to its own file
        with open(output_path, 'w') as ready:
            ready.write(new_letter)
