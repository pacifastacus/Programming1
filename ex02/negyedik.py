# Write a Python program which can open the input.txt
# and  writes back the content  of it into the output.txt.
# It changes the letters from small one to big one and from big one to small one.

def change_lettercase(string: str):
    return_string = ""
    for char in string:
        if char.isupper():
            return_string += char.lower()
        elif char.islower():
            return_string += char.upper()
        else:
            return_string += char
    return return_string


try:
    f_in = open("input.txt", "r")
    f_out = open("output.txt", "w")
    for line in f_in:
        print(change_lettercase(line), file=f_out, end="")
    f_in.close()
    f_out.close()
except FileNotFoundError:
    print("Az input.txt nem létezik!")
