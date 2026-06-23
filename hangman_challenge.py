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
# YOUR CODE HERE

# Wait for 1 second
time.sleep(1)

print('\nStart guessing...') # \n in a string tells python to print a line break, or move to the next line
time.sleep(0.5) # wait for half a second using the sleep function in the time package

# Create a variable called secret_word to store the word to be guessed
# YOUR CODE HERE

# Create a variable called guesses and assign it to an empty string. We'll store the letters the player guesses here
# YOUR CODE HERE

# Create a variable to store the maximum number of turns the game will allow (each incorrect guess will count as a turn)
# YOUR CODE HERE

# Start a while loop and check if we have more than 0 turns available
# YOUR CODE HERE

  # If we have turns available, create a counter variable that starts at 0 to hold the number of incorrect guesses we make
  # YOUR CODE HERE
  
  # Start a for loop and iterate through every character in your secret_word variable
  # YOUR CODE HERE
  
    # As you iterate through each character, 
    # use an if statement to check if the letter is in the player's guess, aka the guesses variable
    # YOUR CODE HERE
      # If it is, print out the character
      # YOUR CODE HERE
    else:
      # If it isn't, print an underscore ...
      print('_', end='') # adding the second parameter end='' tells python not to add a new line at the end
      # ...and increase the failed counter by 1
      # YOUR CODE HERE

  # Check if your incorrect guesses are equal to 0
  # YOUR CODE HERE 
    # If it is, tell the user they've won!
    # YOUR CODE HERE
    # ...then exit the game
    break

  # Otherwise, ask the player to guess another character
  guess = input('\n\nGuess a character: ')

  # Add the player's guess to the guesses variable
  guesses += guess

  # Create an if statement 
  # and check if the guess is not found in the word
  # YOUR CODE HERE 
  
    # Decrease your turns by 1
    # YOUR CODE HERE

    #...and tell the player their guess was wrong
    # YOUR CODE HERE

    # Also tell the player how many turns they have left
    # YOUR CODE HERE
    
    # Create an if statement to check if your turns are equal to 0
    # YOUR CODE HERE

      # If they are, tell the player they've lost
      # YOUR CODE HERE

