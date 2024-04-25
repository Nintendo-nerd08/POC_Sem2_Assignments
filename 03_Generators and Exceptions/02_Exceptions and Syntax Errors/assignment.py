number1 = 0
number2 = 0
answer = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number"))
    answer = number1 / number2
except ZeroDivisionError:
    print("Not able to divide by zero!")
