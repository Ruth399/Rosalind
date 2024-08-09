#very messy code for example
Rosalind_6404 = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
Rosalind_5959 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
Rosalind_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

nucleotides_count_6404 = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

nucleotides_count_5959 = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

nucleotides_count_0808 = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

#Update nucleotide counts for Rosalind_6404
for nucleotide in Rosalind_6404:
    nucleotides_count_6404[nucleotide] += 1

total_6404 = sum(nucleotides_count_6404.values())
print(total_6404)  #.values() displays a list of all the objects and their values in the dictionary
GC_total_6404 = nucleotides_count_6404['G'] + nucleotides_count_6404['C']
print(GC_total_6404)
GC_content_6464 = ((GC_total_6404/total_6404)*100)

#print("Rosalind_6404 GC content is:", ((GC_total_6404/total_6404)*100))  #remember the comma!!! otherwise python interprets the first pair of () after the str as an attempt to call the string as if it were a function

#Update nucleotide counts for Rosalind_5959
for nucleotide in Rosalind_5959:
    nucleotides_count_5959[nucleotide] += 1

total_5959 = sum(nucleotides_count_5959.values())
GC_total_5959 = nucleotides_count_5959['G'] + nucleotides_count_5959['C']  #this has to be inserted after the values in the dictionary have been updated
GC_content_5959 = ((GC_total_5959/total_5959)*100)

print("Rosalind_5959 GC content is:", ((GC_total_5959/total_5959)*100))

# Update nucleotide counts for Rosalind_0808
for nucleotide in Rosalind_0808:
    nucleotides_count_0808[nucleotide] += 1

total_0808 = sum(nucleotides_count_0808.values())
GC_total_0808 = nucleotides_count_6404['G'] + nucleotides_count_5959['C']
GC_content_0808 = ((GC_total_0808/total_0808)*100)

print("Rosalind_0808 GC content is:", ((GC_total_0808/total_0808)*100))

GC_contents = [("GC_content_6464",GC_content_6464), ("GC_content_5959",GC_content_5959), ("GC_content_0808",GC_content_0808)] #tuple containing var name & var value
#sorted_GC_contents = sorted()  # Sort by the second element in each tuple (the value)

#for name, value in sorted_GC_contents:
#    print(f"{name}: {value}")

GC_contents.sort() #-> alternative way of sorting, not the best in this scenario, as i want to return the values with their assigned dna string
print(GC_contents)

#not very effective code 
#second attempt

f = open("/Users/Pete_the_Meme/Desktop/rosalind_gc.txt", "r") #obtained file directory by pressing option once selected file
print(f.readline())
print(f.readline())






