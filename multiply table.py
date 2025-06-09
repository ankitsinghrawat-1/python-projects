a = int(input('Enter a number: '))
print(f"your multiplication table of {a} is:")
x = int(input("starting range for multiply: "))
y = int(input("Ending range for multiply: "))
for i in range(x, y + 1):
    print(f"{a} x {i} = {a * i}")