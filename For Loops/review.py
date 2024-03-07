for x in range(5):
    print(x)

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " -Average: " + str(sum/length))

product = 1
for n in range(1, 10):
    product = product * n
print(product)

def to_celcius(x):
    return (x - 32)*5/9
for x in range(0, 101, 10):
    print(x, to_celcius(x))

name = []