#!/usr/bin/python3
for i in range(10):
    for z in range(10):
        if i == 9 and z == 9:
            print("99")
        if i <= z:
            print("{:d}{:d}".format(i, z), end=", ")
