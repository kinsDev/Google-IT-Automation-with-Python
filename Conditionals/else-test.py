def hint_username(username):
    return username
username = input("Enter your username: ")
if len(username) < 3:
    print("Invalid username. Must be at least 3 characters")
else:
    print("Valid username")