# Using file object own methods for reading and writing
# Read from file
fin = open("input.txt", "r")
n = 5
nchar = fin.read(n)  # Get n char from fin
fin.seek(0)  # <- rewind file stream (like rewind a tape). Generally seek() can be used to reposition the stream

line = fin.readline()  # Get the next line from fin
fin.seek(0)
array_of_lines = fin.readlines()  # Get all the lines from fin. The result is a list object containing all the lines of fin
fin.close()
print("result of:")
print("fin.read(n):", nchar)
print("fin.readline():", line)
print("fin.readlines():", array_of_lines)  # maybe the output of this line is too long. It prints an array of strings

# Write into a file
fout = open("output.txt", "w")
n = 5
res = fout.write("foobar")  # Write "foobar" into the fout file
print("fout.write() returned with:", res)
res = fout.write(
    "spam")  # When we call .write(s) again, s will be writen right after the previous .write() call result  (no newline or any other separation in the file)
fout.close()
fin = open("output.txt", "r")
print(fin.readlines())  # output.txt content
fin.close()
