#!/usr/bin/python3
def uppercase(str):
    for g in str:
        asc = ord(g)
        compute = asc - 32 if (97 <= asc <= 122) else asc
        print("{:c}".format(compute), end="")
    print()
