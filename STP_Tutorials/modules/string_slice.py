import logging
from pathlib import Path

# Use logging rather than print statements to track workflows and record exceptions.py
current_directory = str(Path(__file__).resolve().parent)
logging.basicConfig(level=logging.DEBUG,  # DEBUG, INFO, WARN, ERROR
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler(f"{current_directory}/logs/string_slice.log"),
                              logging.StreamHandler()],)

# logging.info("Find sqrt of {} starting with guess {}".format(x, guess))

"""
Given a string and two pairs of integers, return two slices of the string between the positions represented by the two 
number pairs inclusively

So given a string "TheUniversityOfManchesterFacultyofBiologyMedicineAndHealth" and number pairs 3,13 and 15,25 the 
output will be:

University Manchester
"""


def slice_string(query_string, query_slice_list):
    """
    :param query_string: The String we want to slice
    :param query_slice_list: List of integer for the slices
    :return: The two slices joined by whitespace
    """
    logging.info("Slice string {} at positions {} and {}".format(query_string, str(query_slice_list[0:1]), str(query_slice_list[2:3])))
    slice_1 = query_string[query_slice_list[0]:query_slice_list[1]]

    logging.info("Slice 1 gives {}".format(slice_1))
    slice_2 = query_string[query_slice_list[2]:query_slice_list[3]]

    logging.info("Slice 2 gives {}".format(slice_2))
    return " ".join([slice_1, slice_2])


if __name__ == '__main__':
    """
    This code allows me to directly call the script and use a test string e.g. the one below
    """
    string = "TheUniversityOfManchesterFacultyofBiologyMedicineAndHealth"
    slice_list = [3, 13, 15, 25]
    string_slices = slice_string(string, slice_list)
    print(string_slices)



