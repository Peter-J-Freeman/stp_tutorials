"""
Module that contains functions for validating DNA strings and transcribing DNA strings
"""

# Import modules
import logging
from . import exceptions
from pathlib import Path

# Use logging rather than print statements to track workflows and record exceptions.py
current_directory = str(Path(__file__).resolve().parent)
logging.basicConfig(level=logging.DEBUG,  # DEBUG, INFO, WARN, ERROR
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler(f"{current_directory}/logs/transribe.log"),
                              logging.StreamHandler()],)


def is_dna(dna_sequence):
    """
    Function the determines whether a sequence is DNA, i.e. in the DNA alphabet
    :param dna_sequence:
    :return: True or raise error
    """

    # Check to ensure the submitted sequence it Upper Case
    if not dna_sequence.isupper():
        raise exceptions.SequenceError("DNA sequences should be Upper Case according to the IUPAC Alphabet")

    # Make sure only GATC is used - Note: this currently does not allow for "wobble bases"
    position = 0
    # Loop through the dna sequence
    for i in dna_sequence:
        # Add 1 to the counter
        position += 1

        # Loop through the sequence and raise an exception that tells us the non DNA base and the position in the
        # sequence
        if i not in "GATC":
            raise exceptions.SequenceError("Non DNA base {} at position {}".format(i, str(position)))

    # DNA sequence passes, return True
    return True


def transcribe(dna_sequence, start_position=1):
    """
    Function that translated a DNA string from a designated start position
    :param dna_sequence: (str) query sequence
    :param start_position: (int) the position we transcribe from
    :return:
    """

    # Remove any whitespace by splitting at () which is any white space and immediately re-join the lost into a string
    dna_sequence = "".join(dna_sequence.split())
    logging.info("Transcribe {} from position {}".format(dna_sequence, str(start_position)))

    # Check the sequence is DNA
    is_dna(dna_sequence)

    # Slice out the DNA sequence from the stated start base (-1 to deal with 0 basing) to the end of the sequence
    logging.info("Sequence {} is DNA so transcribe".format(dna_sequence))
    transcribe_this = dna_sequence[start_position - 1:]

    # Replace T with U and lower case into the RNA alphabet
    transcribed_sequence = transcribe_this.replace("T", "U").lower()

    # Return the sequence
    return transcribed_sequence


if __name__ == "__main__":
    from . import exercise_2_1
    string = """
             GCTGAGACTTCCTGUACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACA
             GAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAA
             CCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAA
             CCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT
             """
    transcript = transcribe(string)
    print(exercise_2_1.chunk_string(transcript, 10, 6))



