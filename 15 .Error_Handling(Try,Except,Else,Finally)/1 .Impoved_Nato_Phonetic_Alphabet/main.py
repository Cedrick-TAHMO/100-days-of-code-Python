import pandas as pd
is_good = True

data = pd.read_csv('nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# This error handler is attempting to regulate the user input
# In case of wrong input (e.g. 11223, $#$*&), the code will send an error message
# And prompt the user to try again

while is_good:
    user_word = input("Enter a word: ").upper()
    try:
        name_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError as error:
        print(f"The input {error}, is not valid \nSorry, only letters in the alphabet please.")
    else:
        is_good = False
        print(name_list)