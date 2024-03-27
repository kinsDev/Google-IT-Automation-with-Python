num = int(input("Input: "))
def countBits(num):
    counter = [0]
    if num >=  1:
        while len(counter) <= num:
            counter = counter + [i + 1 for i in counter]
        return counter[:num+1]
    else:
        return 0
print(countBits(int(num)))

# How does the function really work?
"""
1. function countbits calls parameter num which is the user's input
2. we define a counter to start counting the num at index 0
3. if the num is greater than or equal to 1, and the len of the counter is less than num, we increment the counter by 1
4. I don't know hoe to explain or read this code:
counter = counter + [i + 1 for i in counter]
        return counter[:num+1]
    else:
        return 0
-- so help me out on explaining from there!
"""