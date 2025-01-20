# Palingram Finder

`palingram-finder` is a Python tool that detects **palingrams**—pairs of words where one word is the reverse of the other—from a given dictionary. It leverages set-based lookups for efficient performance, even with large word lists.

---

## Features
- **Reverse Word Pair Detection**: Finds pairs of words that are reversed versions of each other.
- **Optimized Performance**: Uses Python sets for fast lookups and duplicate avoidance.
- **Custom Dictionary**: Supports any dictionary file for analysis.
---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/palingram-finder.git

2. Navigate to the project directory:
   ```bash
   cd palingram-finder
---
## Usage

1. Place your dictionary file (e.g., 2of4brif.txt) in the data folder or modify the dictionary path in the script.
2. Run the script:
    ```bash
    python main.py

This will print the reversed word pairs found in the dictionary.
---
## Example

Given a dictionary with words like ["drawer", "reward"], the script will find the following palingram pair:

* drawer and reward
---
## License

This project is open-source [License](https://github.com/imaditya123/palingram-finder?tab=Apache-2.0-1-ov-file)