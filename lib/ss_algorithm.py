from lib.helpers import *

def calculate_score(driver_name: str, street_name: str):
    """Takes a driver name and street name, and calculates suitability score based on given algorthim"""
    suitability_score = 0

    if length_is_even(street_name):
        suitability_score += (count_vowels(driver_name) * 1.5)

    if not length_is_even(street_name):
        suitability_score += count_consonants(driver_name)

    if len(normalize_names(street_name)) == len(normalize_names(driver_name)):
        suitability_score += (suitability_score * 1.5)

    return suitability_score