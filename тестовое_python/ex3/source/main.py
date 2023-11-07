def roman_numerals_to_int(romanNumeral):
    try:
        romanNumbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        romanNumeral = romanNumeral.replace("IV", "IIII").replace("IX", "VIIII")
        romanNumeral = romanNumeral.replace("XL", "XXXX").replace("XC", "LXXXX")
        romanNumeral = romanNumeral.replace("CD", "CCCC").replace("CM", "DCCCC")
        for symbol in romanNumeral:
            result += romanNumbers[symbol]
        return result
    except KeyError:
        return None
    except AttributeError:
        return None


if __name__ == '__main__':
    print(roman_numerals_to_int("MCII"))
