#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
answer = str(number)
if int(answer[-1]) > 5:
    print(f"Last digit of {number} is {answer[-1]} and is greater than 5")
elif int(answer[-1]) == 0:
    print(f"Last digit of {number} is {answer[-1]} and is 0")
else:
    print(f"Last digit of {number} is {answer[-1]} and is less than 6 and not 0")
