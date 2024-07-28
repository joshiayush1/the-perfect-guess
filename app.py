import random

class ThePerfectGuess:
    def __init__(self):
        self.toGuess = random.randint(1, 100)

    def game(self):
        print("THE PERFECT GUESS")
        print("You have to guess a number from 1 to 100 in the fewest attempts")
        print("")  # an empty line
        
        attempts = 0
        userGuess = -1
        while self.toGuess != userGuess:  # loop till user's guess matches the target
            try:
                userGuess = int(input("Guess the number: "))
                attempts += 1

                if userGuess < self.toGuess:
                    print("Higher number please!")
                elif userGuess > self.toGuess:
                    print("Lower number please!")
            except ValueError:
                print("Please enter a valid number.")

        print("You guessed it right!!!")
        print(f"You found the number {self.toGuess} in {attempts} attempts.")

tpg = ThePerfectGuess()
tpg.game()
