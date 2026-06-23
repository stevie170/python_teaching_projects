# Debugger!
# One section at a time, identify the source of the error and debug the code.

# --- Section 1: Dragon Name --- (NameError)
dragon_name = input("What do you want to name your dragon? ")
print("Great! Your dragon's name is " + Dragon_name)

# --- Section 2: Choose Color --- (SyntaxError: missing parentheses)
dragon_color = input("What color is your dragon? "
print(f"{dragon_name} is now a {dragon_color} dragon!")

# --- Section 3: Dragon Length --- (TypeError: can't concat str and int)
length = input("How many feet long is your dragon? ")
print("Wow! " + dragon_name + " is " + length + 0 + " feet long!")

# --- Section 4: Dragon Sounds --- (IndentationError)
sound = input("What sound does your dragon make? ")
    print(f"{dragon_name} says {sound}!")

# --- Section 5: Dragon Fact --- (IndexError or logic bug)
fact = dragon_color[10]
print(f"Did you know the 11th letter of your dragon's color is '{fact}'?")

# --- Section 6: Grand Reveal --- (Everything should now work)
print("Thanks for designing your dragon!")
print(f"{dragon_name} the {dragon_color} dragon is {length} feet long and says {sound}!")

# Bonus 

# Challenge 1: Secret Dragon Mission

print("Your dragon needs to complete a secret mission!")

mission = input("Choose a mission: rescue, treasure hunt, or sky race: ")
print(f"Mission accepted: {mission}.")

speed = input("How fast can your dragon fly (in mph)? ")
print("Preparing flight system...")

# Bug 1: logic + type
boosted_speed = speed + 50
print(f"Boosted flight speed: {boosted_speed} mph")

# Bug 2: name error
print("Ready for takeoff, " + dragon_Name + "!")

# Bug 3: forgotten f-string
print("Mission " + mission + " complete! Your dragon flew at {boosted_speed} mph!")

"""
# Challenge 2: Dragon IQ Test
# can you identify and fix the bugs?

name = input("Enter your dragon's name: ")
iq = input("Enter your dragon's IQ score: ")

if iq > 100:
    print(f"{name} is a genius dragon!")
else:
print(f"{name} is still awesome, just in a different way.")
"""
