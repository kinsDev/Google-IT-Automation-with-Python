x = 10
while x % 2 == 0:
    x = x / 2
    print(x)

def do_something_cool(xyz):
    print(xyz)

    while True:
        if user_requested_to_stop():
            break

        result = some_action_to_repeat()
        print(result)

    return result
# Assuming there's a function user_requested_to_stop() defined somewhere
def user_requested_to_stop():
    # Assuming this function checks if the user wants to stop
    # Return True or False based on user input or some condition
    pass

# Assuming there's a function some_action_to_repeat() defined somewhere
def some_action_to_repeat():
    # Assuming this function performs some action you want to repeat
    # Replace this with the actual action you want to repeat
    pass

# Example usage:
do_something_cool("Huuuuuray!")