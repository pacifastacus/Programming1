# 1

# 2 

# 3
def count_Lanister(f):
	pass #Write your code here!

try:
	file = open("input.txt","r")
	c = count_Lanister(file)
	file.close()
	print("A 'Lannister' szóv előfordulása a szövegben:{:d}".format(c))
except FileNotFoundError:
	print("Az input.txt állomány nem létezik!")
# 4

# 5
