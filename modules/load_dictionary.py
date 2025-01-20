import sys


def load(file_path: str) -> list:
    try:
        with open(file_path, "r") as file:
            return [word.lower() for word in file.read().strip().splitlines()]
    except IOError as e:
        print(f"Error opening {file_path}: {e}\nTerminating program.", file=sys.stderr)
        sys.exit(1)
