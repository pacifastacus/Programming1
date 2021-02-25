# Write a Python program to print out a set containing all the colors from color_list_1 which
# are not present in color_list_2. The program gets the lists via commandline argument as:
# “L:” “White” “Black” “Red” “L:” “Red” “Green”
# est Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

import sys

list1 = []
list2 = []
flag = 0
for arg in sys.argv[1:]:
    if arg == "L:":
        flag += 1
        continue
    if flag == 1:
        list1.append(arg)
    elif flag == 2:
        list2.append(arg)

color_list_1 = set(list1)
color_list_2 = set(list2)
result = color_list_1.difference(color_list_2)
print(result)
