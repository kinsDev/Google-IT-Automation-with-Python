sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)
        x += 1
        print(new_list) #updates the new list after every iteration
print("\n")
print(new_list) #updates the final list after all the iterations are done with

print("\n")
#list comprehension
sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]
print(new_list)