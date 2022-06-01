#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(8):
        for j in range(10):
            if i < j:
                print("{:d}{:d}, ".format(i, j), end="")
    print(89)
