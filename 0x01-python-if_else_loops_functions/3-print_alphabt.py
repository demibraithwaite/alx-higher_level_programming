#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(97, 123):
        if i == 101 or i == 113:
            continue
        print("{:c}".format(i), end="")
