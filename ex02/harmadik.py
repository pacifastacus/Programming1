# Write a Python function that accepts an opened file object as
# input and give back the number of “Lannister” in the file

def count_Lannister(file):
    count = 0
    for line in file:
        tmp = line.split()
        for word in tmp:
            if 'Lannister' in word:
                count += 1
    return count


try:
    file = open("input.txt", "r")
    count = count_Lannister(file)
    file.close()
    print('A "Lannister" szavak száma a szövegben:', count)
except FileNotFoundError:
    print("input.txt is not exists")
