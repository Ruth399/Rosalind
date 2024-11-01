DNA_bases = 'GTGCCGTGGCGATAGCTTCGCCTTCGTGCGGAGGGCTCTAATCATGTCCCGAATTCAAAATAGAAGCCCTCCCCATCGAGGATTCGGGGGGCCAGGGGATAGTTCACGGCGTGGCATCAGAAAGAGGAAGATAAGCCCGTGAAGGGCGAAGCGATTACCTACCAGTGTTTGCATTAGACACTTGGGCTATGGATGCCCTCACATTGTCTATGGTATTATGCAAGTGGCTCGTGGCAATCGATCCAAAAACGAATCTAGTCGGCGGGTAAGAACGCCCATATACGGCTTGTGTAAAACCTATAGTAATGTCTACGTTATTATTTCCAAGAGAACTAAAGGAGTTCTCTTACTTTTTTAAGGCGCTATCTTCTTCAGTGCACTAGTCTCACGAAGTCTCATAATCAGGCATCGACATTTCCGCCACATCAAGTCAGTAACTATAAGATGGGTTCATGAGTAGGCGTCATGCGGCATAATACTTTGCCCAGCTAGGAGGTCAGCTCCTGATTGATCAACCCAAGATCCGTTGGCACAACTCACTGTGGTGGGTGATGCAGACTACCTTGTAGCAAGCCAAACGTCTTGCCGGTATTCTACTTACTGATCAAAACGGAGCATTGATGGGGCCCAAGCCTACCTCGCTGGGATACGAGGTGTTGCCAATGGATGATAGCGTGTCCGATACTTACGTACACAGCTATTTGTCTTCAGCGGGGAACATTTTCTTCCGGCCAAATACCGTTGGCACCTGAGGACCGGTTCGCTTGCGAATTAGCGCTGCGCCGCGGCATGTCCCCCTGGTTTTAAATGTAGACCCGTGGTTATATTGAGGCTAGCCTTGTCCGCTCGTCTATCTTGTGGTCATGGTCCTCCTC'

nucleotides = list(DNA_bases)

nucleotides_count = {}

for word in nucleotides:
    if word in nucleotides_count:
        nucleotides_count[word] += 1
    else:
        nucleotides_count[word] = 1
for word, count in nucleotides_count.items():
    print(word + ' ' + str(count))

#DNA_bases_count = {}

#for word in DNA_bases['nucleotides'].splitlines(''):
 #   print(word)

 #Alternative method

DNA_bases1 = 'GTGCCGTGGCGATAGCTTCGCCTTCGTGCGGAGGGCTCTAATCATGTCCCGAATTCAAAATAGAAGCCCTCCCCATCGAGGATTCGGGGGGCCAGGGGATAGTTCACGGCGTGGCATCAGAAAGAGGAAGATAAGCCCGTGAAGGGCGAAGCGATTACCTACCAGTGTTTGCATTAGACACTTGGGCTATGGATGCCCTCACATTGTCTATGGTATTATGCAAGTGGCTCGTGGCAATCGATCCAAAAACGAATCTAGTCGGCGGGTAAGAACGCCCATATACGGCTTGTGTAAAACCTATAGTAATGTCTACGTTATTATTTCCAAGAGAACTAAAGGAGTTCTCTTACTTTTTTAAGGCGCTATCTTCTTCAGTGCACTAGTCTCACGAAGTCTCATAATCAGGCATCGACATTTCCGCCACATCAAGTCAGTAACTATAAGATGGGTTCATGAGTAGGCGTCATGCGGCATAATACTTTGCCCAGCTAGGAGGTCAGCTCCTGATTGATCAACCCAAGATCCGTTGGCACAACTCACTGTGGTGGGTGATGCAGACTACCTTGTAGCAAGCCAAACGTCTTGCCGGTATTCTACTTACTGATCAAAACGGAGCATTGATGGGGCCCAAGCCTACCTCGCTGGGATACGAGGTGTTGCCAATGGATGATAGCGTGTCCGATACTTACGTACACAGCTATTTGTCTTCAGCGGGGAACATTTTCTTCCGGCCAAATACCGTTGGCACCTGAGGACCGGTTCGCTTGCGAATTAGCGCTGCGCCGCGGCATGTCCCCCTGGTTTTAAATGTAGACCCGTGGTTATATTGAGGCTAGCCTTGTCCGCTCGTCTATCTTGTGGTCATGGTCCTCCTC'

nucleotides_count1 = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

for item in DNA_bases1:
    nucleotides_count1 += 1

for item in ['A', 'C', 'G', 'T']:
    print(item + nucleotides_count1[item])