from pathlib import Path
import sys
import pytest
sys.path.append(str(Path(__file__).resolve().parent.parent))
from STP_Tutorials.modules import string_slice, sum_odd_integers, exercise_1_4, exercise_1_5, exercise_2_1, exceptions


def test_string_slice():
    string = "TheUniversityOfManchesterFacultyofBiologyMedicineAndHealth"
    slice_list = [3, 13, 15, 25]
    return_value = string_slice.slice_string(string, slice_list)
    assert return_value == "University Manchester"


def test_sum_odd_integers():
    odd_integers_summed = sum_odd_integers.sum_odd_integers(a=50, b=100)
    assert odd_integers_summed == 1875


def test_exercise_1_4():
    chunk_string = "aggagtaagcccttgcaactggaaatacacccattg"
    assert exercise_1_4.chunk_string(chunk_string, 3) == "agg agt aag ccc ttg caa ctg gaa ata cac cca ttg"
    assert exercise_1_4.chunk_string(chunk_string, 5) == "aggag taagc ccttg caact ggaaa tacac ccatt g"


def test_exercise_1_5():
    chunk_string = """
             GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACA
             GAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAA
             CCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAA
             CCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT
             """
    transcript = exercise_1_5.transcribe(chunk_string)
    chunked = exercise_2_1.chunk_string(transcript, 10, 6)
    assert """1 gcugagacuu ccuggacggg ggacaggcug ugggguuucu cagauaacug ggccccugcg\n""" in chunked


def test_exercise_1_5_non_dna_base():
    chunk_string = """
             GCTGAGACTTCCTGUACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACA
             GAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAA
             CCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAA
             CCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT
             """
    with pytest.raises(exceptions.SequenceError) as exc_info:
        exercise_1_5.transcribe(chunk_string)
        assert str(exc_info.value) == "Non DNA base U at position 15"


def test_exercise_1_5_with_rna():
    chunk_string = """gatcggga"""

    with pytest.raises(exceptions.SequenceError) as exc_info:
        exercise_1_5.transcribe(chunk_string)
        assert str(exc_info.value) == "DNA sequences should be Upper Case according to the IUPAC Alphabet"
