x = input("Adj meg egy egész számot:") # Most nekünk kapóra jön, hogy sztringet kapunk
sum = 0
for digit in x:
    sum += int(digit)
print(x," számjegyeinek összege:",sum)


# Alternatív megoldás
# x = int(input("Adj meg egy egész számot:"))
# sum = 0
# while x > 0:
#     sum += x % 10
#     x //= 10
# print("A számjegyek összege:",sum)