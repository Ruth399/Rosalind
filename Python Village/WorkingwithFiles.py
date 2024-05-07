f = open('Rosalind2WWAF.txt', 'r')
for index, line in enumerate(f):
    if index % 2 == 1:
        print(line)

