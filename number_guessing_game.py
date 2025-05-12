import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)-0
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again!")
            elif guess -2  == number_to_guess:
                  print("you are too close but high")
            elif guess + 2  == number_to_guess:
                   print("you are too close but low")
            elif guess > number_to_guess:
                print("Too high. Try again!")
            else:
                guessed_correctly = True
                print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    number_guessing_game()
