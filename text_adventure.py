def text_adventure():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest. Your goal is to find your way out safely.")
    print("Make your choices wisely.\n")

    def choice_1():
        print("You see a path splitting into two.")
        print("1. Take the left path.")
        print("2. Take the right path.")
        while True:
            choice = input("Enter 1 or 2: ")
            if choice == "1":
                return "left"
            elif choice == "2":
                return "right"
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def choice_2_left():
        print("\nYou took the left path and encounter a river.")
        print("1. Try to swim across.")
        print("2. Look for a bridge.")
        while True:
            choice = input("Enter 1 or 2: ")
            if choice == "1":
                print("\nYou try to swim but the current is too strong. You drown. Game over.")
                return "end"
            elif choice == "2":
                print("\nYou find a bridge and cross safely.")
                return "bridge_crossed"
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def choice_2_right():
        print("\nYou took the right path and meet a mysterious stranger.")
        print("1. Talk to the stranger.")
        print("2. Ignore and keep walking.")
        while True:
            choice = input("Enter 1 or 2: ")
            if choice == "1":
                print("\nThe stranger gives you a map. You find your way out easily. You win!")
                return "end"
            elif choice == "2":
                print("\nYou get lost and wander forever. Game over.")
                return "end"
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def choice_3_bridge():
        print("\nAfter crossing the bridge, you see a cabin.")
        print("1. Enter the cabin.")
        print("2. Keep walking past the cabin.")
        while True:
            choice = input("Enter 1 or 2: ")
            if choice == "1":
                print("\nInside the cabin, you find food and rest. You survive the night and find your way out the next day. You win!")
                return "end"
            elif choice == "2":
                print("\nYou get caught in a storm and can't find shelter. Game over.")
                return "end"
            else:
                print("Invalid choice. Please enter 1 or 2.")

    path = choice_1()
    if path == "left":
        result = choice_2_left()
        if result == "bridge_crossed":
            choice_3_bridge()
    elif path == "right":
        choice_2_right()

if __name__ == "__main__":
    text_adventure()
