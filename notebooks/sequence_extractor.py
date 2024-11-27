import os

def sequence_extractor_for_all_files(data_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the data folder
    for fasta_file in os.listdir(data_folder):
        # Construct the full path to the file
        fasta_path = os.path.join(data_folder, fasta_file)

        # Check if it is a file (skip directories)
        if os.path.isfile(fasta_path) and fasta_file.endswith(".fasta"):
            # Process the file
            print(f"{fasta_file} done")  # Optional: for tracking progress
            sequence_extractor(fasta_file, data_folder, output_folder)

def sequence_extractor(fasta_file, data_folder, output_folder):
    # Full path to the input FASTA file
    fasta_path = os.path.join(data_folder, fasta_file)

    with open(fasta_path, 'r') as f:
        title = ''
        sequence = ''

        for line in f:
            line = line.strip()  # Remove any leading/trailing whitespace

            if line.startswith(">"):  # Header line (sequence identifier)
                # If there's a previous sequence, save it to a file
                if title and sequence:
                    # Create a file named after the sequence identifier (title)
                    sequence_file = os.path.join(output_folder, f"{title}.txt")
                    with open(sequence_file, 'w') as seq_file:
                        seq_file.write(sequence)  # Write only the sequence (not the header)

                # Extract the accession number from the header
                parts = line.split()  # Split by whitespace
                title = parts[0][1:]  # Remove the ">" and get the accession number
                sequence = ''  # Reset sequence for the next entry

            else:  # Sequence line (nucleotide data)
                if line.startswith(('A', 'C', 'T', 'G')):
                    sequence += line  # Add the sequence to the current sequence

        # After the loop, save the last sequence
        if title and sequence:
            sequence_file = os.path.join(output_folder, f"{title}.txt")
            with open(sequence_file, 'w') as seq_file:
                seq_file.write(sequence)  # Write only the sequence (not the header)


# Example usage:
data_folder = 'data'  # Folder where the raw FASTA files are located
output_folder = 'sequences'  # Folder where the sequences will be saved

# Process all FASTA files in the directory
sequence_extractor_for_all_files(data_folder, output_folder)
