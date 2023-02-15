#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    total = 0
    sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(roman_string)):
        if i == len(roman_string) - 1:
            total += sym[roman_string[i]]
        elif sym[roman_string[i]] >= sym[roman_string[i + 1]]:
            total += sym[roman_string[i]]
        elif sym[roman_string[i]] < sym[roman_string[i + 1]]:
            total -= 10**(len(str(sym[roman_string[i]])) - 1)
    return total
