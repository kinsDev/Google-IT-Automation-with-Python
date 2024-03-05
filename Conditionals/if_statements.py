def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 character long")
        return False
    else:
        return True

username = input("Enter username: ")
if not hint_username(username):
    new_username = input("Enter a new username: ")
    if hint_username(new_username):
        print("Username updated successfully!")
    else:
        print("Invalid username. Must be at least 3 characters long")


