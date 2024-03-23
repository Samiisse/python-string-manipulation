#Write a Python program to find the length of the longest word in a sentence

def longest_word_length(sentence):
    """
    Find the length of the longest word in a given sentence.

    Parameters:
        sentence (str): The input sentence.

    Returns:
        int: The length of the longest word.
    """
    # Split the sentence into words
    words = sentence.split()
    # Initialize the length of the longest word
    max_length = 0
    # Iterate through each word and update max_length if needed
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
    return max_length

# Example usage:
input_sentence = "The quick brown fox jumps over the lazy dog"
longest_length = longest_word_length(input_sentence)
print("Length of the longest word in the sentence:", longest_length)
