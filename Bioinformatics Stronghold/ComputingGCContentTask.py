
with open("/Users/Ruth Legesse/Desktop/rosalind_gc(2).txt", "r") as file:
    DNA_bases = file.read()

entries = DNA_bases.split('>')[1:]  


dna_dictionary = {}


for entry in entries:
    lines = entry.splitlines()  
    identifier = lines[0]  
    sequence = ''.join(lines[1:]).replace(" ", "").replace("\n", "").replace("\t", "").strip()  
    sequence = sequence.upper()  
    sequence = ''.join([char for char in sequence if char in 'ATCG']) 
    
    
    print(f"Processing {identifier}:")
    print(f"Full sequence: {sequence}")
    print(f"Length of sequence: {len(sequence)}\n")
    
    if not sequence:  
        print(f"Skipping empty sequence for identifier: {identifier}")
        continue
    dna_dictionary[identifier] = sequence  


def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_count = len(dna_sequence)
    
   
    print(f"Sequence: {dna_sequence[:50]}...")  
    print(f"GC count: {gc_count}, Total count: {total_count}")
    
    if total_count == 0:
        return 0
    gc_content = (gc_count / total_count) * 100
    return gc_content


gc_contents = {identifier: calculate_gc_content(sequence) for identifier, sequence in dna_dictionary.items()}


sorted_gc_contents = sorted(gc_contents.items(), key=lambda x: x[1], reverse=True)


for identifier, gc_content in sorted_gc_contents:
    print(f"{identifier}: {gc_content:.6f}%")
