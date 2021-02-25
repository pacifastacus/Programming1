# Write a Python program which gets a filename and a number from the commandline
# argument and write a method to generate a given number random integer from [0-100]
# interval and save them to the file and write a function to sum the numbers from the file.

import random
import sys


def sum_in_file(file):
    sum = 0
    for line in file:
        sum += int(line)
    return sum


def generate_random_numbers(n, outfile):
    for i in range(n):
        print(random.randint(0, 100), file=outfile)


try:
    fname = sys.argv[1]
    n = int(sys.argv[2])
    f = open(fname, "w+")
    generate_random_numbers(n, f)
    f.seek(0)
    sum = sum_in_file(f)
    print("A számjegyek összege a {} fájlban: {}".format(fname, sum))
    f.close()
except IndexError:
    print("Két argumentumot (fájlnév szám) várok")
except ValueError:
    print("A második argumentum egy szám kell legyen!")
except FileNotFoundError:
    print("A megadott fájlnév nem létezik!")
