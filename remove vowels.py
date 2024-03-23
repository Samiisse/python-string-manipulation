#Given a string, write a function to remove all vowels from it and return the modified string

def remove_vowel(string):
    vowels = ['a' , 'e' , 'i' , 'o' , 'u']
    result = [letter for letter in string if letter.lower() not in vowels] 
    result = ''.join(result) 
    print(result)

string = "What is your name"
remove_vowel(string)