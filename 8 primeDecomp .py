def smallest_prime_factor(n):
    # Check if n is divisible by 2
    if n % 2 == 0:
        return 2

    # Check odd numbers from 3 to square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i

    # If no factor is found, n is prime
    return n


def prime_decomposition(n):
    factors = []

    # Find the smallest prime factor iteratively
    while n != 1:
        smallest_factor = smallest_prime_factor(n)
        factors.append(smallest_factor)
        n //= smallest_factor

    return factors


# Get user input for the number
num = int(input("Enter an integer: "))

# Calculate the prime decomposition
decomposition = prime_decomposition(num)

# Print the prime decomposition
print("Prime decomposition of", num, "is:", end=" ")
print(*decomposition, sep=" x ")
