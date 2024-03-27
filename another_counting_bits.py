def countBits(num):
    counter = [0]
    if num >= 1:
        while len(counter) <= num:
            new_counts = [i + 1 for i in counter]
            counter.extend(new_counts)
        return counter[:num+1]
    else:
        return 0
def main():
    num = int(input("Input: "))
    print("Output: ", countBits(num))
if __name__ == "__main__":
    main()