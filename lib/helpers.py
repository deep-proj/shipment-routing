"""Series of helper functions that return useful data points or cleanup data for calculations"""

def normalize_names(name: str):
    """Takes in a string, name, removes all white spaces and converts to lower case."""
    normalized_name = name.replace(" ", "").lower()
    return normalized_name

def length_is_even(name: str):
    """Takes in a string, name, passes it to normalize_names, and returns true if the numerical length of the string is even"""
    name = normalize_names(name)
    length = len(name)
    return True if length % 2 == 0 else False

def count_vowels(name: str):
    """Takes a string, name, and returns the number of vowels in the string"""
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    name = normalize_names(name)
    for i in range (len(name)):
        if name[i] in vowels:
            count += 1
    return count

def count_consonants(name: str):
    """Takes a string, name, and returns the number of consonants in the string"""
    name = normalize_names(name)
    count = len(name) - count_vowels(name)
    return count
