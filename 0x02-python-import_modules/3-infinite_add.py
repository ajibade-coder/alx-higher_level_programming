#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = len(argv) - 1
    if total == 0:
        print("{}".format(0))
    else:
        answer = 0
        for x in range(total):
            answer += int(argv[x + 1])
        print("{}".format(answer))
