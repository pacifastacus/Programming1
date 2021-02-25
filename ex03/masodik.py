# Write a python program which gets the n number and the name of the output file from
# the commandline argument and write a method to sum of the first n positive integers and
# write the whole equation into the file.
# 1+2+3+4+5=15

import sys


def sum_first_n_ints(n, outfile):
    sum = 0
    s = ''
    for num in range(1, n + 1):
        sum += num
        s += str(num) + "+"
    s = s[:-1] + '=' + str(sum)
    print(s, file=outfile)


try:
    n = int(sys.argv[1])
    file_path = sys.argv[2]
    fout = open(file_path, "w")
    sum_first_n_ints(n, fout)
    fout.close()
except IndexError:
    print("Két argumentumra van szükségem!")
except IOError:
    print("Nem tudom megnyitni a fájlt írásra")
