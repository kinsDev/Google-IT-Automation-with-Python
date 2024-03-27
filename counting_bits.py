num = int(input("Input: "))
def countBits(num):
    counter = [0]
    if num >= 1:
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
3. if the num is greater than or equal to 1, and the len of the counter is less than num
4. We iterate over each element in the counter list and adding 1 to it hence doubling the values in the counter list
5. we append the newly created list(double values) to the counter list  essentially doubling the size of the counter list
6. we return all the number in the counter list inclusive of the last number in the counter list 
"""