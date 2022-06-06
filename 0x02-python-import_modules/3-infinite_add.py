#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1
    if arg_len == 0:
        print(0)
    else:
        addup = sum(map(int, [word for word in argv if word != argv[0]]))
        print(addup)
