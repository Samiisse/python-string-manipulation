#Given a list of words, concatenate them into a single string separated by spaces

def concatenate_words(word_list):
    """
    Concatenate a list of words into a single string separated by spaces.

    Parameters:
        word_list (list): The list of words to concatenate.

    Returns:
        str: The concatenated string.
    """
    # Join the words in the list with spaces
    concatenated_string = ' '.join(word_list)
    return concatenated_string

# Example usage:
word_list = ["Hello", "world", "from", "Python"]
result = concatenate_words(word_list)
print("Concatenated string:", result)