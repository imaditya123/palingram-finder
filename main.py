import sys
from modules.load_dictionary import load
from modules.find_palingram import find_palingram


def main():
    # Specify your dictionary path here
    dictionary_path = "data/2of4brif.txt"  # Adjust the path if needed
    find_palingram(dictionary_path)


# Main execution point
if __name__ == "__main__":
    main()
