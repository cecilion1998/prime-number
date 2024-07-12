def is_prime(num):
    # Check if the number is less than 2
    if num < 2:
        return False
    # Check for factors other than 1 and the number itself
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Example usage:
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
