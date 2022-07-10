# This will be a calculator

num1 = float(input("Enter a number: "))
op = input("Enter operator number: ")
num2 = float(input("Enter another number: "))

op2 = input("Enter operator number: ")
num4 = float(input("Enter another number: "))

num3 = ""

if op == "+":
    num3 = num1 + num2
elif op == "-":
    num3 = num1 - num2
elif op == "/":
    num3 = num1 / num2
elif op == "*":
    num3 = num1 * num2
else:
    print("invalid operator")


if op2 == "+":
    print(num3 + num4)
elif op2 == "-":
    print(num3 - num4)
elif op2 == "/":
    print(num3 / num4)
elif op2 == "*":
    print(num3 * num4)
else:
    print("invalid operator")


# Usefulness: Computer generally don't have calculator unless you search on internet

# I have a better understanding on  how to use and apply "if,elif,else" and "float" function in a real world project
# though the process of making this calculator

