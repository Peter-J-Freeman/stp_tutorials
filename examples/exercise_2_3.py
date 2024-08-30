"""
Module that reverse complements DNA strings
"""

import logging
from . import exercise_1_5
from pathlib import Path

# Use logging rather than print statements to track workflows and record exceptions.py
current_directory = str(Path(__file__).resolve().parent)
logging.basicConfig(level=logging.DEBUG,  # DEBUG, INFO, WARN, ERROR
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler(f"{current_directory}/logs/reverse_complement.log"),
                              logging.StreamHandler()],)


def reverse(dna_string):
    """
    Reverse a DNA string
    :param dna_string:
    :return:
    """
    # Check the string is DNA
    exercise_1_5.is_dna(dna_string)

    # Reverse the string using slice offset to -1 for the full string
    return dna_string[::-1]


def complement(dna_string):
    """
    Complement a DNA string
    :param dna_string:
    :return: (str)
    """
    # Check the string is DNA
    exercise_1_5.is_dna(dna_string)

    # This line of code joins together a for loop that returns a list that complements the bases while iterating
    return "".join([{"G": "C", "T": "A", "A": "T", "C": "G"}[base] for base in list(dna_string)])


def reverse_complement(dna_seq):
    """
    Reverse complement a DNA string using the
    :param dna_seq:
    :return: (str)
    """
    reverse_seq = reverse(dna_seq)
    complement_sequence = (complement(reverse_seq))
    return complement_sequence


if __name__ == '__main__':
    """
    This code allows me to directly call the script and use a test string e.g. the one below
    """
    dna_sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC"
    reverse_sequence = reverse(dna_sequence)
    print(reverse_sequence)
    print("\n")
    print(complement(reverse_sequence))
    print("\n")
    print(reverse_complement(dna_sequence))
