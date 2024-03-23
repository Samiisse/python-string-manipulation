#Create a program that checks if a given string is a palindrome.

def is_palindrome(s):
    """
    Check if a given string is a palindrome.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
