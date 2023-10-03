#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
answer = str(number)
answer = int(answer[-1])
if int(answer) > 5:
    print(f"Last digit of {number} is {answer} and is greater than 5")
elif int(answer) == 0:
    print(f"Last digit of {number} is {answer} and is 0")
else:
    print(f"Last digit of {number} is {answer} and is less than 6 and not 0")
