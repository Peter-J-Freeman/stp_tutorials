from . import string_slice
from . import sum_odd_integers
from . import exercise_1_4


def test_string_slice():
    string = "TheUniversityOfManchesterFacultyofBiologyMedicineAndHealth"
    slice_list = [3, 13, 15, 25]
    return_value = string_slice.slice_string(string, slice_list)
    assert return_value == "University Manchester"


def test_sum_odd_integers():
    odd_integers_summed = sum_odd_integers.sum_odd_integers(a=50, b=100)
    assert odd_integers_summed == 1875


def test_chunking():
    chunk_string = "aggagtaagcccttgcaactggaaatacacccattg"
    assert chunking.chunk_string(chunk_string, 3) == "agg agt aag ccc ttg caa ctg gaa ata cac cca ttg"
    assert chunking.chunk_string(chunk_string, 5) == "aggag taagc ccttg caact ggaaa tacac ccatt g"
