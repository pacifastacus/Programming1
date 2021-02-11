# 1

while True:
	try:
		x = input("Adj meg egy egész számot:")
		x = int(x)
		break
	except ValueError:
		print("A megadott bemenet ({}) nem alakítható egész számmá!".format(x))

# 2 
try:
	fpath = input("Kérem a fájl elérési útját:")
	f = open(fpath,"r")
	for line in f:
		print(line)
	f.close()
except IOError:
	print("A megadott fájl nem létezik!")
		
# 3
def count_Lanister(f):
	count = 0
	for line in f:
		tmp = line.split()
		for word in tmp:
			if 'Lannister' in word:
				count += 1
	return count

try:
	file = open("input.txt","r")
	c = count_Lanister(file)
	file.close()
	print("A 'Lannister' szóv előfordulása a szövegben:{:d}".format(c))
except FileNotFoundError:
	print("Az input.txt állomány nem létezik!")

# 4
def inverse_string_case(string: str):
	ret_string = ""
	for ch in string:
		# if 'A' <= char <= 'Z':
		if ch.isupper():
			ret_string += ch.lower()
		# elif 'a' <= char <= 'z':
		elif ch.islower():
			ret_string += ch.upper()
		else:
			ret_string += ch

	return ret_string

try:
	in_file = open("input.txt","r")
	out_file = open("output.txt","w")
	for line in in_file:
		print(inverse_string_case(line),file=out_file)
	in_file.close()
	out_file.close()
except FileNotFoundError:
	print("A megadott fájl nem létezik!")


# 5
def get_longest_words(str_list: list):
	#Módosítsuk úgy, hogy ismétlődő szavak ne legyenek benne az eredményben
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
		#Mi a különbség az append és az extend között?
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
