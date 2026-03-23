import os

# Global codon table
CODON_TABLE = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}

def sequence_extractor_for_all_files(data_folder, output_folder):

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the data folder
    for txt_file in os.listdir(data_folder):
        txt_path = os.path.join(data_folder, txt_file)

        # Check if it is a valid .txt file
        if os.path.isfile(txt_path) and txt_file.endswith(".txt"):
            print(f"Processing {txt_file}...")
            sequence_extractor(txt_file, data_folder, output_folder)

def sequence_extractor(txt_file, data_folder, output_folder):

    txt_path = os.path.join(data_folder, txt_file)

    # Read the DNA sequence from the file
    with open(txt_path, 'r') as f:
        dna_sequence = f.read().strip()  # Read and remove any surrounding whitespace

    # Translate the DNA sequence to a protein sequence
    protein_sequence = translate(dna_sequence)

    # Write the protein sequence to the output file
    output_path = os.path.join(output_folder, txt_file)  # Keep the same filename
    with open(output_path, 'w') as out_file:
        out_file.write(protein_sequence)

def translate(seq):

    protein = ""
    # Process the sequence in codons (triplets)
    for i in range(0, len(seq) - len(seq) % 3, 3):  # Ignore trailing incomplete codons
        codon = seq[i:i + 3]
        protein += CODON_TABLE.get(codon, 'X')  # Use 'X' for unknown codons
    return protein


# Input and output directories
input_folder = "dna_sequences"  # Folder containing input .txt files
output_folder = "aa_sequences"  # Folder to store output .txt files

# Run the sequence extraction and translation
sequence_extractor_for_all_files(input_folder, output_folder)
