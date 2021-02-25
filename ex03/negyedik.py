# Write a Python program which gets a string from the commandline argument and write a
# function to count the number of occurrence of a specific character in a string.

import sys


def character_occurs(string, char):
    count = 0
    if len(char) > 1:
        raise Exception("The second parameter is not a character!")

    for c in string:
        if c == char:
            count += 1
    return count


if len(sys.argv) < 3:
    print("Adj meg argumentumként egy stringet és karaktert!")
    quit()

c = character_occurs(sys.argv[1], sys.argv[2])

print("A '{}' karakter előfordulásainak száma a '{}' karakterláncban {}".format(sys.argv[2], sys.argv[1], c))
