try:
    n= int(input("Enter a number: "))

except ValueError:
    print("Error: Invalid input. Please enter integers only.")

try:
    m = int(input("Enter another number: "))
    if m < 0:
        print("Error: The second number must be non-negative.")
        

except ValueError:
    print("Error: Invalid input. Please enter integers only.")

def closest(n=n, m=m):

    for i in range(n):
        rem = n % m
        if n > 0:
            if rem == 0:
                print(f"The closest no. to {n} that is divisible to {m} is {n}")

            elif 
      


closest(n, m)