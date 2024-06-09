Rosalind_6404 = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"

Rosalind_5959 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"

Rosalind_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"


nucleotides_count_6404 = {'A':0, 'T':0, 'C':0, 'G':0}

nucleotides_count_5959 = {'A':0, 'T':0, 'C':0, 'G':0} 

nucleotides_count_0808 = {'A':0, 'T':0, 'C':0, 'G':0}

for nucleotide in Rosalind_6404:
    nucleotides_count_6404[nucleotide] += 1

for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"Rosalind_6404 {nucleotide} : {nucleotides_count_6404[nucleotide]}")

for nucleotide in Rosalind_5959:
    nucleotides_count_6404[nucleotide] += 1

for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"Rosalind_5959 {nucleotide} : {nucleotides_count_5959[nucleotide]}")

for nucleotide in Rosalind_0808:
    nucleotides_count_6404[nucleotide] += 1

for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"Rosalind_0808 {nucleotide} : {nucleotides_count_0808[nucleotide]}")


Rosalind_6404 = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
Rosalind_5959 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
Rosalind_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

nucleotides_count_6404 = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
nucleotides_count_5959 = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
nucleotides_count_0808 = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

# Update nucleotide counts for Rosalind_6404
for nucleotide in Rosalind_6404:
    nucleotides_count_6404[nucleotide] += 1

# Print nucleotide counts for Rosalind_6404
for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"Rosalind_6404 {nucleotide}: {nucleotides_count_6404[nucleotide]}")

# Update nucleotide counts for Rosalind_5959
for nucleotide in Rosalind_5959:
    nucleotides_count_5959[nucleotide] += 1

# Print nucleotide counts for Rosalind_5959
for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"Rosalind_5959 {nucleotide}: {nucleotides_count_5959[nucleotide]}")

# Update nucleotide counts for Rosalind_0808
for nucleotide in Rosalind_0808:
    nucleotides_count_0808[nucleotide] += 1

# Print nucleotide counts for Rosalind_0808
for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"Rosalind_0808 {nucleotide}: {nucleotides_count_0808[nucleotide]}")
