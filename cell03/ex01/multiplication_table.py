#!/usr/bin/env python3

num = int(input("Enter a number\n"))

for i in range(0, 10):
    mult = num * i
    print(str(i) + " x " + str(num) + " = " + str(mult))