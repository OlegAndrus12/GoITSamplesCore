import random                      # Import the random module 

number = random.randrange(1, 1000) # Get random number between [1 and 1000)
guesses = 0
guess = int(input("Guess my number between 1 and 1000: "))

while guess != number:
    guesses += 1
    if guess > number:
        print(guess, "is too high.") 
    elif guess < number:
        print(guess, " is too low.")
    guess = int(input("Guess again: "))

print("\n\nGreat, you got it in", guesses,  "guesses!")