# Import modules
import logging  # For logging info, warnings, errors, and debug statements
from pathlib import Path  # For working with file system paths

# Determine the directory where this script is located
current_directory = str(Path(__file__).resolve().parent)

# Set up logging configuration
# - Logs messages to both a file and the console
# - File is saved in a 'logs' folder within the script's directory
# - Logging level is set to DEBUG (can be changed to INFO, WARNING, etc.)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"{current_directory}/logs/chunking.log"),  # Log to file
        logging.StreamHandler()  # Also log to console
    ]
)


def chunk_string(query_sequence, chuk_by):
    """
    Split a DNA sequence into evenly sized chunks.

    Parameters:
    query_sequence (str): The DNA sequence string to be split.
    chuk_by (int): The length of each chunk.

    Returns:
    str: A string of space-separated chunks.
    """
    logging.info("Chunk {} into blocks of {}".format(query_sequence, str(chuk_by)))

    # Initialize a list to hold each chunk
    my_list = []

    # This is a DEBUG-level message; useful for development or troubleshooting
    logging.debug("This is a critical print statement which I can switch off by increasing the log level")

    # Loop through the sequence, taking slices of length `chuk_by` until empty
    while query_sequence:
        # Take the first `chuk_by` characters and add to the list
        my_list.append(query_sequence[:chuk_by])
        # Remove those characters from the sequence
        query_sequence = query_sequence[chuk_by:]

    # Join the chunks with spaces and return the result
    return my_list


# Run this block if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Example DNA sequence
    string = "aggagtaagcccttgcaactggaaatacacccattg"
    # Desired chunk length
    chunk_length = 5
    # Output the chunked string
    print(" ".join(chunk_string(string, chunk_length)))

