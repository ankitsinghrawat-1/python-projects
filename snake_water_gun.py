import random

choices = ["snake", "water", "gun"]

cpoints = 0
upoints = 0

while True:
        uchoice = input("Enter your choice (snake, water, gun) or 'exit' to quit the game: ").lower()

        if uchoice == 'exit' or uchoice == 'quit':
            print("Exiting the game...")
            print("Thanks for playing!")
            print("Game Over")
            print(f"Final Scores are like this: Your points: {upoints} \n Computer points: {cpoints}")
            if upoints > cpoints:
                print("Congratulations! You win the game!")
            elif cpoints > upoints:
                print("Computer wins the game!")
            else:
                print("It's a tie!")
            break

        if uchoice not in choices:
            print("Invalid choice. Please choose from snake, water, or gun.")
            continue

        cchoice = random.choice(choices)
        print(f"Computer chose: {cchoice}")

        if uchoice == cchoice:
            print(f"Both players selected {uchoice}. It's a tie!")

        elif uchoice == 'snake' and cchoice == 'water':
            print("Snake drinks water. You win!")
            upoints +=1
            

        elif uchoice == 'water' and cchoice == 'gun':
            print("Water extinguishes gun. You win!")
            upoints +=1

        elif uchoice == 'gun' and cchoice == 'snake':
            print("Gun shoots snake. You win!")
            upoints +=1

        else:
            print(f"Computer wins! {cchoice} beats {uchoice}.")
            cpoints += 1

print(f"Your points: {upoints}, Computer points: {cpoints}")