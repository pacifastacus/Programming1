# Write a Python program to find the longest words in the input.txt and write the word and
# the length of it into the longestWord.txt. If there are more than one longest word, the
# program writes all of them into the output file.


def get_longest_words(str_list: list):
    # Módosítsuk úgy, hogy ismétlődő szavak ne legyenek benne az eredményben
    maxlength = 0
    ret_words = []
    for word in str_list:
        if len(word) > maxlength:
            maxlength = len(word)
            ret_words.clear()
            ret_words.append(word)
        elif len(word) == maxlength:
            ret_words.append(word)
    return ret_words, maxlength


words_in_file = []
try:
    f = open("input.txt", "r")
    for line in f:
        # Mi a különbség az append és az extend között?
        words_in_file.extend(line.split())
    f.close()
except FileNotFoundError:
    print("A megadott fájl nem létezik!")

longest_words, length = get_longest_words(words_in_file)
try:
    f = open("longestword.txt", "w")
    print("A leghosszab szó hossza ", length, file=f)
    for word in longest_words:
        print(word, file=f)
    f.close()
except IOError:
    print("HIBA")
