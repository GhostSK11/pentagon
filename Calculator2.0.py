# Updated version of the first calculator, with operation options

print("Calculator 2.0")
a = float(input("Insert the first number: "))
b = float(input("Insert the second number: "))
print("Choose one of the following operations:")
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
option = int(input(""))

# The elif keyword is used in conditional statements (if statements), and is short for else if.
if (option == 1):
        result = a + b
elif (option == 2):
        result = a - b
elif (option == 3):
        result = a * b
elif (option == 4):
        result = a / b
if option > 0 and option < 5:
        print("Result: %f" % (result))
else:
        print("Incorrectly option")
print("Press any button")