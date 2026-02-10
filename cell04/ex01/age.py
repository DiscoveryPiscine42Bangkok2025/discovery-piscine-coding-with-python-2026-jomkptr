#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
print("You are currently " + str(age) + " years old.")

for i in range(10, 40, 10):
    new_age = age + i
    print("In " + str(i) + " years, you'll be " + str(new_age) + " years old.")