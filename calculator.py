a = int(input("Enter a number: "))

operators = ['Addition', 'Subtraction', 'Division', 'Multiplication', 'power']

opera = ["+", "-", "/", "*", "**"]


for i in range(len(operators)):
    print(f"{i + 1}. {operators[i]}")

op = int(input("Enter the number of operator you to perform with the given numbers: "))

b = int(input("Enter a second number: "))

def add(a, b):
    ans = (a + b)
    print(ans)

def subtract(a, b):
    ans = (a - b)
    print(ans)

def multiply(a, b):
    ans = (a * b)
    print(ans)

def divide(a, b):
    ans = (a // b)
    print(ans)

def power(a, b):
    ans = (a ** b)
    print(ans)

while op != 'quit' or op != 'exit' :
    with open("History.txt", "a") as f:
        if op == 1:
            f.write(f"{a} {opera[0]} {b} = {a + b}\n")
        elif op == 2:
            f.write(f"{a} {opera[1]} {b} = {a - b} \n")
        elif op == 3:
            f.write(f"{a} {opera[2]} {b} = {a / b}\n")
        elif op == 4:
            f.write(f"{a} {opera[3]} {b} = {a * b}\n")
        elif op == 5:
            f.write(f"{a} {opera[4]} {b} = {a ** b} \n")

    try:
        if op == 1:
            add(a,b)

        if op == 2:
            subtract(a, b)

        if op == 3:
            divide(a, b)

        if op == 4:
            multiply(a, b)

        if op == 5:
            power(a, b)

        if op == 'quit' or op != 'exit':
            break


    except ValueError:
        print("Enter a valid option")