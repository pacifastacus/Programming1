# Write a Python program to read an entire text file line by line and it writes them to the consol.
# It can handle the FileNotFoundError.

try:
    fname = input("Adja meg a beolvasandó fájl elérési útját:")
    file = open(fname, "r")
    for i, line in enumerate(file):
        print(i + 1, ". ", line, sep="",
              end="")  # line.strip() can be used to remove newline from read lines, instead of telling print() not to end output with (another) newline.
    file.close()

except FileNotFoundError:
    print("A megadott fájl nem létezik! (Talán elgépelte?)")

print("A fájl beolvasása megtörtént")
