program_name = sys.argv[0]
print('The name of my program is', program_name)
print(len(sys.argv))
for x in sys.argv[1:]:
    print(x)
