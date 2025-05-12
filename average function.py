def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)
num = input("enter the number:")
numbers= map(float, num.split())
c= average(*numbers)
print(c)