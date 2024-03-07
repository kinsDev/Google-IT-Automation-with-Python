def is_power_of_two(number):
    while number % 2 == 0:
        number += 2
    if number == 1:
        return True
    return False


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier < 5:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1