def first_n(string: str, n: int) -> str:
    if len(string) < 3:
        return string
    else:
        return string[:n]


s = input("sztring >")
n = int(input("n >"))
print(first_n(s,n))