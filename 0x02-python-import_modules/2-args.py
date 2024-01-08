#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argumentString = "{:d} argument"
argumentCount = len(sys.argv) - 1
if argumentCount == 0:
    argumentString += 's.'
elif argumentCount == 1:
    argumentString += ':'
else:
    argumentString += 's:'
print(argumentString.format(argumentCount))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
