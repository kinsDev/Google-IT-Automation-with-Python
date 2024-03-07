x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("Yeah, finally!!! We are at x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
        print("Done")
attempts(5)

username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()