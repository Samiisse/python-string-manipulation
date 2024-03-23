#Write a program that takes a sentence as input and counts the number of words in it

def count_words(sentence):
    """
    Count the number of words in a given sentence.

    Parameters:
        sentence (str): The input sentence.

    Returns:
        int: The number of words in the sentence.
    """
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    # Return the count of words
    return len(words)

# Example usage:
input_sentence = input("Enter a sentence: ")
word_count = count_words(input_sentence)
print("Number of words in the sentence:", word_count)
