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

original_num = int(input("Enter a number: "))
num = original_num
roman_numeral = ""

for number, roman in RomanNumerals.items():
    while num >= number:
        roman_numeral += roman
        num -= number

print("Input: num = ", original_num)
print("Output: ", roman_numeral)

# Provide an explanation of the output
print("Explanation:", end=" ")
for char in roman_numeral:
    if char in RomanNumerals.values():
        print(char, "=", list(RomanNumerals.keys())[list(RomanNumerals.values()).index(char)], end=". ")
print()