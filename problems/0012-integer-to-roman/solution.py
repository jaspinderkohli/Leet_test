class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        # start with an empty string to hold the Roman numeral representation of the number
        roman_numeral = ""
        
        # loop through the dictionary in reverse order to ensure that larger Roman numerals are used first
        for value in sorted(roman_numerals.keys(), reverse=True):
            # divide the number by the current Roman numeral value and get the quotient and remainder
            quotient, num = divmod(num, value)
            # add the corresponding number of Roman numerals to the final representation
            roman_numeral += quotient * roman_numerals[value]
            
        # return the final representation of the number as a Roman numeral
        return roman_numeral
