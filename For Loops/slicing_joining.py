string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

print(string1[-10:]) # Prints “Earthlings” again - python counts from end of string if it is negative
print("\n")

# How to combine slicing and joining strings
phonenum = "2025551212"
# The first 3 digits are the area code
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[6:]
    return area_code + " " + exchange + "-" + line
print(format_phone(phonenum))
print("\n")

# Phone number details
PhoneNumber = input("Enter your phone: ")
def thePhoneNumber(PhoneNumber):
    code = "(" + PhoneNumber[:3] + ")"
    exch = PhoneNumber[3:6]
    lin = PhoneNumber[6:]
    return code + exch + "-" + lin
print(thePhoneNumber(PhoneNumber))