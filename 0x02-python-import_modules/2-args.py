#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[1]))
    else:
        print("{} arguments:".format(argc))
        comb = [f"{i}: {lin}"for i, lin in enumerate(argv) if lin != argv[0]]
        print("\n".join(comb))
