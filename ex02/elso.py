# Write a Python program which asks the user for input until a valid integer has been entered.

while True:
    try:
        x = input("Adj meg egy egész számot:")
        x = int(x)
        break
    except ValueError:
        print("A megadott input {} nem alakítható egész számmá!".format(x))
