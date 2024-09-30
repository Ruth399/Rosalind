with open("/Users/Ruth Legesse/Desktop/rosalind_gc(1).txt", "r") as file:
    DNA_bases = file.read()#.replace("\n", "")
    #print(DNA_bases) #DNA_bases contains a string, and the .readline() object cannot be attributed to it

entries = DNA_bases.split('>')[1:]

dna_dictionary = {}

for entry in entries:
    lines = entry.strip().splitlines()  
    identifier = lines[0]  
    sequence = ''.join(lines[1:])  
    dna_dictionary[identifier] = sequence

#print(entries)

#for key, value in dna_dictionary.items():
    #print(f"{key}: {value[:50]}...")

def calculate_gc_content(dna_sequence):
    if len(dna_sequence) == 0:
        return 0.0
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_count = len(dna_sequence)
    gc_content = (gc_count / total_count) * 100
    return gc_content

gc_contents = {identifier: calculate_gc_content(sequence) for identifier, sequence in dna_dictionary.items()}

sorted_gc_contents = sorted(gc_contents.items(), key = lambda x: x[1], reverse = True)

for identifer, gc_content in sorted_gc_contents:
    print(f"{identifier}: {gc_content:.6f}%")
