#Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.

def is_word_present(sentence, word):
    """
    Check if a given word is present in a given sentence.

    Parameters:
        sentence (str): The input sentence.
        word (str): The word to check for in the sentence.

    Returns:
        bool: True if the word is present in the sentence, False otherwise.
    """
    # Split the sentence into words
    words_in_sentence = sentence.split()
    # Check if the word is present in the list of words
    return word in words_in_sentence

# Example usage:
input_sentence = input("Enter a sentence: ")
input_word = input("Enter a word to check for: ")
if is_word_present(input_sentence, input_word):
    print("The word is present in the sentence.")
else:
    print("The word is not present in the sentence.")
