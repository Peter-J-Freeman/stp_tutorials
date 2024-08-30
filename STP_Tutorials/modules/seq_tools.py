"""
Module that contains an object for manipulating DNA strings
"""

import logging
from pathlib import Path

# Use logging rather than print statements to track workflows and record exceptions.py
current_directory = str(Path(__file__).resolve().parent)
logging.basicConfig(level=logging.DEBUG,  # DEBUG, INFO, WARN, ERROR
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler(f"{current_directory}/logs/transribe_n_translate.log"),
                              logging.StreamHandler()],)


# Custom exceptions.py
class SequenceError(Exception):
    pass


"""

"""


class SequenceTools:
    def __init__(self):
        self.translation_codes = {}
        self.base_complement = {"G": "C", "T": "A", "A": "T", "C": "G"}
        self.dna_alphabet = "GATC"
        self.rna_alphabet = "gauc"

    def is_dna(self, dna_sequence):
        if not dna_sequence.isupper():
            raise SequenceError("DNA sequences should be Upper Case according to the IUPAC Alphabet")
        position = 0
        for i in dna_sequence:
            position += 1
            if i not in self.dna_alphabet:
                raise SequenceError("Non DNA base {} at position {}".format(i, str(position)))
        return True

    def is_rna(self, rna_sequence):
        if not rna_sequence.islower():
            raise SequenceError("RNA sequences should be Lower Case according to the IUPAC Alphabet")
        position = 0
        for i in rna_sequence:
            position += 1
            if i not in self.rna_alphabet:
                raise SequenceError("Non RNA base {} at position {}".format(i, str(position)))
        return True

    def reverse_complement(self, dna_string):

        # Check the string is DNA
        self.is_dna(dna_string)

        # Reverse the string using slice offset to -1 for the full string and list to convert into a list
        reverse_bases = list(dna_string[::-1])

        # This line of code joins together a for loop that returns a list that complements the bases while iterating
        complement = "".join([self.base_complement[base] for base in reverse_bases])

        return complement


if __name__ == '__main__':
    """
    This code allows me to directly call the script and use a test string e.g. the one below
    """
    # st = SequenceTools()
    # dna = "GATC"
    # rna = "aggagtaagcccttgcaactggaaatacacccattg"
    # print(st.transcribe(dna))

    # Create object
    seq_tools = SequenceTools()

    dna_sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC"
    reverse_complement = seq_tools.reverse_complement(dna_sequence)
    print(reverse_complement)
