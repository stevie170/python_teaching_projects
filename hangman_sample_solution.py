# Hangman (page 165)
"""
Using everything you have learned, try finishing this hangman game!
We have the structure here, but we need to fill in the blanks!
"""

# importing the time package
import time

# Welcome the user and capture their name in a name variable
name = input('What is your name? ')

# Use a print function to greet the user by their name
print(f'Hi {name}!')

# Wait for 1 second
time.sleep(1)

print('\nStart guessing...') # \n in a string tells python to print a line break, or move to the next line
time.sleep(0.5) # wait for half a second using the sleep function in the time package

# Create a variable called secret_word to store the word to be guessed
secret_word = 'hangman'

# Create a variable called guesses and assign it to an empty string. We'll store the letters the player guesses here
guesses = ''

# Create a variable to store the maximum number of turns the game will allow (each incorrect guess will count as a turn)
max_turns = 5

# Start a while loop and check if we have more than 0 turns available
while max_turns > 0:
  

  # If we have turns available, create a counter variable that starts at 0 to hold the number of incorrect guesses we make
  failed = 0
  
  # Start a for loop and iterate through every character in your secret_word variable
  for letter in secret_word:
    
    # As you iterate through each character, 
    # use an if statement to check if the letter is in the player's guess, aka the guesses variable
    if letter in guesses:
      # If it is, print out the character
      print(letter, end='')
    else:
      # If it isn't, print an underscore ...
      print('_', end='') # adding the second parameter end='' tells python not to add a new line at the end
      # ...and increase the failed counter by 1
      failed += 1

  # Check if your incorrect guesses are equal to 0
  if failed == 0: 
    # If it is, tell the user they've won!
    print('\nYou won!')
    print()
    # ...then exit the game
    break

  # Otherwise, ask the player to guess another character
  guess = input('\n\nGuess a character: ')

  # Add the player's guess to the guesses variable
  guesses += guess
  print(f'Here is what you have guessed so far: {guesses}')
  
  # Create an if statement 
  # and check if the guess is not found in the word
  if not guess in secret_word: 
  
    # Decrease your turns by 1
    max_turns -= 1

    #...and tell the player their guess was wrong
    print('Wrong')

    # Also tell the player how many turns they have left
    print(f'You have {max_turns} more guesses.')
    
    # Create an if statement to check if your turns are equal to 0
    if max_turns == 0:

      # If they are, tell the player they've lost
      print('Sorry, you have lost.')

