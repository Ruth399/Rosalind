
with open("/Users/Ruth Legesse/Desktop/rosalind_gc(2).txt", "r") as file:
    DNA_bases = file.read()

entries = DNA_bases.split('>')[1:]  # Skip the first empty element

# Dictionary to hold DNA sequences by their identifiers
dna_dictionary = {}

# Process each entry
for entry in entries:
    lines = entry.splitlines()  # Split by lines
    identifier = lines[0]  # First line is the identifier
    sequence = ''.join(lines[1:]).replace(" ", "").replace("\n", "").replace("\t", "").strip()  # Clean and join the sequence
    sequence = sequence.upper()  # Standardize to uppercase
    sequence = ''.join([char for char in sequence if char in 'ATCG']) 
    
    # Print the identifier and sequence for verification
    print(f"Processing {identifier}:")
    print(f"Full sequence: {sequence}")
    print(f"Length of sequence: {len(sequence)}\n")
    
    if not sequence:  # Skip empty sequences
        print(f"Skipping empty sequence for identifier: {identifier}")
        continue
    dna_dictionary[identifier] = sequence  # Store in the dictionary

# Function to calculate GC content
def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_count = len(dna_sequence)
    
    # Debugging: Print the counts for G and C
    print(f"Sequence: {dna_sequence[:50]}...")  # Print only the first 50 characters for readability
    print(f"GC count: {gc_count}, Total count: {total_count}")
    
    if total_count == 0:
        return 0
    gc_content = (gc_count / total_count) * 100
    return gc_content

# Calculate GC content for each sequence and store in a dictionary
gc_contents = {identifier: calculate_gc_content(sequence) for identifier, sequence in dna_dictionary.items()}

# Sort the sequences by GC content in descending order
sorted_gc_contents = sorted(gc_contents.items(), key=lambda x: x[1], reverse=True)

# Print each identifier and its GC content with 6 decimal places
for identifier, gc_content in sorted_gc_contents:
    print(f"{identifier}: {gc_content:.6f}%")
