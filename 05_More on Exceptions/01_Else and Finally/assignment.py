#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number"))
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    answer= number1/number2
    print(answer)- number1/number2
except ZeroDivisionError:
    print("divison by zero is not possible")
finally: 
    print("division taken care of")
