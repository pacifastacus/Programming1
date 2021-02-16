def unique_words(words: str):
    wordlist = words.split(sep=", ")
    wordlist.sort()
    newlist = []
    for word in wordlist:
        if word not in newlist:
            newlist.append(word)
    return newlist

list_of_words = "red, white, black, red, green, black"
print(unique_words(list_of_words))