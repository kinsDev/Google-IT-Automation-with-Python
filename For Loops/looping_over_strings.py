greeting = "Hello"
for letter in greeting:
    print(letter)
print("\n")

# position of the string
for i in range(len(greeting)):
    print(i)
print("\n")

print(len(greeting))
print("\n")

# while loop with indexing
index = 0
while index < len(greeting):
    print(greeting[index])
    index += 1
print("\n")

# while loop with slicing
i = 0
while i < len(greeting):
    print(greeting[i:i+1])
    i += 1
print("\n")
