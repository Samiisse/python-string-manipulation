#Write a function to count the number of vowels in a given string.

def count_vowels(s):
    """
    Count the number of vowels in a given string.

    Parameters:
        s (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    # Define vowels
    vowels = "aeiouAEIOU"
    # Initialize a count variable
    count = 0
    # Iterate through each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            # Increment the count if it is a vowel
            count += 1
    return count

# Example usage:
input_string = "Hello World"
num_vowels = count_vowels(input_string)
print("Number of vowels in the string:", num_vowels)

