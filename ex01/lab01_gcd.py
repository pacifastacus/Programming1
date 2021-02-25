import math

#Euklideszi algoritmus naiiv kivonogatásokkal
def GCD_naiive(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

#Euklideszi algoritmus moduláris aritmetikával
def GCD_proper(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

#Lista egyedi elemeinek rendezett listája 'set()'-el
def UniqueSortedWords(wordlist):
    wordset = set(wordlist)
    newlist = list(wordset).sort()
    return newlist

