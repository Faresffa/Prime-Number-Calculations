def is_prime_by_sqrt(number):
    if number <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, int(number**0.5) + 1):  # Test divisors up to the square root
        if number % i == 0:
            return False
    return True

# Example usage
n = int(input("Enter a number: "))
if is_prime_by_sqrt(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
