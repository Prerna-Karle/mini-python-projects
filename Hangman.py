import random
from words import words
import string

def get_valid_word(words):
    word = str(random.choice(words))  # Convert number to string
    while '-' in word or ' ' in word:
        word = str(random.choice(words))  # Convert again

    return word.upper()  # Ensure consistency with ascii_uppercase

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        print('You have used these letters: ', ' '.join(used_letters))

        # What current word is (i.e W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

# gets here when len(word_letters) == 0
hangman()
