#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    total = len(argv) - 1
    if total !=  3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num1 = int(argv[1])
        num2 = int(argv[3])
        if argv[2] == "+":
            print("{} {} {} = {}".format(num1, argv[2], num2, add(num1, num2)))
        elif argv[2] == "-":
            print("{} {} {} = {}".format(num1, argv[2], num2, sub(num1, num2)))
        elif argv[2] == "*":
            print("{} {} {} = {}".format(num1, argv[2], num2, mul(num1, num2)))
        elif argv[2] == "/":
            print("{} {} {} = {}".format(num1, argv[2], num2, div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
