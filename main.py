import sys
from modules import load
from modules import find_palingram


def main():
    # Specify your dictionary path here
    print(r"""
  ____            _ _                              
 |  _ \ __ _  ___| | |_ __ ___   __ _ _ __   ___  
 | |_) / _` |/ __| | | '_ ` _ \ / _` | '_ \ / _ \ 
 |  __/ (_| | (__| | | | | | | | (_| | | | |  __/ 
 |_|   \__,_|\___|_|_|_| |_| |_|\__,_|_| |_|\___| 
    """)
    print("=== Welcome to Palingram Finder ===")
    dictionary_path = "data/2of4brif.txt"  # Adjust the path if needed
    find_palingram(dictionary_path)


# Main execution point
if __name__ == "__main__":
    main()
