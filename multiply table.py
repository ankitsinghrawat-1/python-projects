
while True:

    a = (input('Enter a number: '))

    if a == 'quit' or a == 'exit':
        print("Exiting the multiplication table program.")
        break
    if not a.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    b = int(a)

    x = int(input("starting range for multiply: "))
    y = int(input("Ending range for multiply: "))

    print(f"your multiplication table of {b} is:")
    for i in range(x, y + 1):
        print(f"{b} x {i} = {b * i}")