#Given a list of names, count the number of names that start with a vowel

def count_names_starting_with_vowel(names):
    """
    Count the number of names in a list that start with a vowel.

    Parameters:
        names (list): The list of names.

    Returns:
        int: The number of names that start with a vowel.
    """
    # Define vowels
    vowels = "aeiouAEIOU"
    # Initialize count
    count = 0
    # Iterate through each name in the list
    for name in names:
        # Check if the first character of the name is a vowel
        if name[0] in vowels:
            count += 1
    return count

# Example usage:
name_list = ["Alice", "Bob", "Eve", "Oscar", "Ursula"]
num_names_starting_with_vowel = count_names_starting_with_vowel(name_list)
print("Number of names starting with a vowel:", num_names_starting_with_vowel)
