# Integer to roman
RomanNumerals = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

num = int(input("Enter a number: "))
roman_numeral = ""

for value, numeral in RomanNumerals.items():
    while num >= value:
        roman_numeral += numeral
        num -= value

print("Output: ", roman_numeral)
