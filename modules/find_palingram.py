from .load_dictionary import load


def find_palingram(dictionary_path: str = "data/2of4brif.txt"):
    # Load the word list and convert to a set for fast lookups
    word_list = set(load(dictionary_path))
    palingrams = set()  # Use a set to avoid duplicates

    # Iterate through the word list
    for word in word_list:
        rev_word = word[::-1]
        end = len(word)

        if end > 1:  # Only process words with length greater than 1
            for i in range(1, end):  # Start from 1 to avoid full matches
                # Check if the suffix of 'word' matches the prefix of 'rev_word'
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in word_list:
                    palingrams.add((word, rev_word[end - i :]))

                # Check if the prefix of 'word' matches the suffix of 'rev_word'
                if word[:i] == rev_word[end - i :] and rev_word[: end - i] in word_list:
                    palingrams.add((rev_word[: end - i], word))

    # Print the result
    print(f"Length of the palingrams found: {len(palingrams)}")
    
    # Print each palingram pair found
    for first, second in palingrams:
        print(f"{first} {second}")
