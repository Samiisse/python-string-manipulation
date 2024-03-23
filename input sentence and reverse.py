#Create a function that takes a sentence as input and returns the sentence in reverse order

def reverse_sentence(sentence):
    """
    Reverse the order of words in a given sentence.

    Parameters:
        sentence (str): The input sentence.

    Returns:
        str: The reversed sentence.
    """
    # Split the sentence into words
    words = sentence.split()
    # Reverse the order of words
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage:
input_sentence = "The quick brown fox jumps over the lazy dog"
reversed_sentence = reverse_sentence(input_sentence)
print("Original sentence:", input_sentence)
print("Reversed sentence:", reversed_sentence)
