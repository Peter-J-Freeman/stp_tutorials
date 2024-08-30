import logging
from pathlib import Path

# Use logging rather than print statements to track workflows and record exceptions.py
current_directory = str(Path(__file__).resolve().parent)
logging.basicConfig(level=logging.DEBUG,  # DEBUG, INFO, WARN, ERROR
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler(f"{current_directory}/logs/genbank_style.log"),
                              logging.StreamHandler()],)


def chunk_string(query_sequence, chuk_by, num_blocks):
    """
    Function to split sequence string into chunks of a value
    :param query_sequence: DNA sequence
    :param chuk_by: Integer. Chunk by
    :param num_blocks: Integer, number of blocks required per line
    :return:
    """
    logging.info("Chunk {} into rows of {} blocks of {}".format(query_sequence, str(num_blocks), str(chuk_by)))

    query_sequence = "".join(query_sequence.split()).lower()  # This line splits the string at all whitespace, joins it
    # together again with no gaps and transforms to lower cases to match the requested output

    full_list = []
    inner_list = []
    while query_sequence:
        if len(inner_list) == num_blocks:  # When the inner list length reaches the number of blocks (tested by len)
            full_list.append(inner_list)   # Append the inner list to the full list and blank the inner list
            inner_list = []
        inner_list.append(query_sequence[:chuk_by])
        query_sequence = query_sequence[chuk_by:]

    if len("".join(inner_list)) < (num_blocks * chuk_by):  # Test, is there an incomplete row  remaining in inner list
        full_list.append(inner_list)

    counter = 0
    text_out = ""
    for line in full_list:
        counter = counter + 1
        row = " ".join(line)
        text_out += "{} {}{}".format(str(counter), row, "\n")
        counter = counter + (len("".join(row.split()))-1)
    return text_out


if __name__ == "__main__":
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
    chunk_length = 10
    block_length = 6
    print(chunk_string(string, chunk_length, block_length))
