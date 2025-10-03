def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

def is_odd(number):
    """Returns True if the number is odd, False otherwise."""
    return not is_even(number)