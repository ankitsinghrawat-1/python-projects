n = int(input("enter a number to find the sum of all numbers from 1 to n: "))

def sumofN(n):
    if n < 1:
        return 0
    else:
        return n + sumofN(n - 1)

print(sumofN(10))