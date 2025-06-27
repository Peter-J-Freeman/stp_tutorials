import logging
from pathlib import Path

# Set up logging to record both to a file and the console
# This helps in debugging and tracking usage without print statements
current_directory = str(Path(__file__).resolve().parent)

logging.basicConfig(
    level=logging.DEBUG,  # Adjust this to INFO or WARNING to reduce output verbosity
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"{current_directory}/logs/genbank_style.log"),  # Log file location
        logging.StreamHandler()  # Also print to console
    ]
)


def chunk_string(query_sequence, chuk_by, num_blocks):
    """
    Formats a DNA sequence into GenBank-style lines:
    Each line contains `num_blocks` blocks of length `chuk_by`, with a counter at the start.

    Parameters:
    query_sequence (str): The DNA sequence to be formatted
    chuk_by (int): The length of each chunk/block
    num_blocks (int): Number of blocks per line

    Returns:
    str: Formatted string in GenBank-style
    """
    logging.info("Chunking sequence into rows of {} blocks of {}".format(num_blocks, chuk_by))

    # Remove all whitespace and convert sequence to lowercase
    query_sequence = "".join(query_sequence.split()).lower()

    full_list = []   # List to hold all rows (each row is a list of blocks)
    inner_list = []  # Temporary list to build a single row

    while query_sequence:
        if len(inner_list) == num_blocks:
            # Current row is full, so add it to the full list and reset
            full_list.append(inner_list)
            inner_list = []
        # Append the next chunk to the current row
        inner_list.append(query_sequence[:chuk_by])
        # Remove the chunk from the sequence
        query_sequence = query_sequence[chuk_by:]

    # Add any remaining blocks in inner_list that didn't make a full row
    if inner_list:
        full_list.append(inner_list)

    counter = 0       # Keeps track of total base count, used for the GenBank-style line prefix
    text_out = ""     # Final formatted output string

    for line in full_list:
        counter += 1  # Line prefix is 1-based index of first base, mimicking GenBank format
        row = " ".join(line)  # Join blocks with spaces
        text_out += "{}\t{}{}".format(str(counter), row, "\n")

        # Update the counter to reflect total bases seen so far
        # (row.split() removes whitespace; ''.join(...) gives total base count in this line)
        counter += len("".join(row.split())) - 1

    return text_out


# Example usage if script is run directly
if __name__ == "__main__":
    # Multiline string simulating a DNA sequence input (could be from FASTA or GenBank)
    string = """\
    GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC
    CTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAA
    GAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGG
    AACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAA
    AGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTT
    AGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAA
    ACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCA
    AAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAA
    ACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAAC
    CTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTA
    TTGCAGTGTGGGAGATCAAGTAAATAAAAAAAAAAAA"""

    chunk_length = 10   # Length of each chunk (e.g., block of 10 bases)
    block_length = 6    # Number of blocks per line (e.g., 6 blocks of 10 bases = 60 bases per line)

    # Print the formatted sequence
    print(chunk_string(string, chunk_length, block_length))
