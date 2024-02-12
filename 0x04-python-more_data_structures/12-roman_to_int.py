#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    if len(roman_string) == 1:
        return roman_dict[roman_string]
    number = 0
    total = 0
    for i in reversed(roman_string):
        number = roman_dict[i]
        if total < number * 5:
            total += number
        else:
            total -= number
    return total
