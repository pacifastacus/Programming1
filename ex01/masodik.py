x = input("Adj meg két számot szőközzel elválasztva:")
a, b = x.split()
a = int(a) # ez legyen a kisebb
b = int(b) # ez legyen a nagyobb

if a > b:
    a, b = b, a

div = 1
for n in range(1, a+1):
    if a%n == 0 and b%n == 0:
        div = n

print("A legnagyobb közös osztó:",div)
