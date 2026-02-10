#!/usr/bin/env python3

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
mult = num1 * num2

print(str(num1) + " x " + str(num2) + " = " + str(mult))

if mult == 0:
    print("The result is positive and negative.")
elif mult > 0:
    print("The result is positive.")
else:
    print("The result is negative.")