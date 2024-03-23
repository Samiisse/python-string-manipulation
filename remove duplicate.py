# Write a function to remove all duplicate characters from a given string

def remove_duplicates(input_string):
    """
    Remove all duplicate characters from a given string.

    Parameters:
        input_string (str): The input string.

    Returns:
        str: The string with duplicate characters removed.
    """
    # Create an empty set to store unique characters
    unique_chars = set()
    # Initialize an empty string to store the result
    result_string = ""
    # Iterate through each character in the input string
    for char in input_string:
        # Add the character to the result string if it's not already in the set
        if char not in unique_chars:
            result_string += char
            unique_chars.add(char)
    return result_string

# Example usage:
input_string = "hello world"
result = remove_duplicates(input_string)
print("String with duplicates removed:", result)
