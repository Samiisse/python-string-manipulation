#implement a function that checks if a given string is a pangram (contains all letters of the alphabet)

def is_pangram(sentence):
    """
    Check if a given sentence is a pangram (contains all letters of the alphabet).

    Parameters:
        sentence (str): The input sentence to check.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    # Create a set of lowercase alphabets
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    # Convert the sentence to lowercase and remove non-alphabetic characters
    sanitized_sentence = ''.join(char.lower() for char in sentence if char.isalpha())
    # Check if the set of unique letters in the sanitized sentence is equal to the alphabet set
    return set(sanitized_sentence) == alphabet_set

# Example usage:
input_sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
