n = int(input("Enter a number: "))
def fibonacci(n):
    if n  < 0:
        return "Input should be a positive integer."
    if n == 0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")