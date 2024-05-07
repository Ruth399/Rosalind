#f.read(n) - returns bytes of files as a string
#f.readline() - returns a single line from the file, followed by \n (newline character), this can be removed using .strip()
#f.readlines() - returns a list of every line in the file 
#f.readlines()[x] - returns a specific line in the file (remember python uses 0-based numbering system)

#f = open('WWAF1.rtf', 'r')
#for line in f:
 #   if line % 2 == 0: 
  #      print(line)


with open('WWAF1.rtf', 'r') as f:
    for index, line in enumerate(f):
        if index % 2 == 0:
            print(line)

#an alternative way of printing every other line - need to explore the false line a bit more
f = open('WWAF1.rtf', 'r')
print_line = False
for line in f:
    if print_line:
        print(line)
    print_line = not print_line
f.close()

#an alternative way of printing every other line
with open('WWAF1.rtf', 'r') as f:
    lines = f.readlines()
    for line in lines[1::2]: #slicing - 1 is the starting element, and then :: tells the program to skip every two elements
        print(line)

