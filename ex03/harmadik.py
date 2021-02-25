# Write a Python program which gets a big integer (seconds) and the name of output file from the
# commandline argument and write a method to convert the seconds to day, hour, minutes
# and seconds.

import sys


def secondsToTime(seconds, outFile):
    tmp = seconds
    year = seconds // (3600 * 24 * 365)
    seconds = seconds % (3600 * 24 * 365)
    day = seconds // (3600 * 24)
    seconds = seconds % (3600 * 24)
    hour = seconds // 3600
    seconds = seconds % 3600
    min = seconds // 60
    seconds = seconds % 60
    print(
        "{} másodperc megfelel {} év {} nap {} óra {} perc {} másodperc időtartamnak".format(tmp, year, day, hour, min,
                                                                                             seconds),
        file=outFile)


try:
    seconds = int(sys.argv[1])
    file_path = sys.argv[2]
    fout = open(file_path, "w")
    secondsToTime(seconds, fout)
except IndexError:
    print("Két argumentumra (másodpercek, fájlnév) van szükségem!")
