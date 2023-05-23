def isPrime(x):
    # Check if the number is less than 2, which is not prime
    if x < 2:
        return False

    # Check for divisibility from 2 to the square root of x
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True


def printPrimesInRange(a, b):
    primes = []

    # Iterate through each number in the range
    for num in range(a, b + 1):
        # Check if the current number is prime
        if isPrime(num):
            primes.append(num)

    # Print the prime numbers in the range
    print("Prime numbers between", a, "and", b, "are:")
    print(primes)


def printTwinPrimesInRange(a, b):
    twin_primes = []

    # Iterate through each number in the range
    for num in range(a, b + 1):
        # Check if the current number and the next number are both prime
        if isPrime(num) and isPrime(num + 2):
            twin_primes.append((num, num + 2))

    # Print the twin primes in the range
    print("Twin primes between", a, "and", b, "are:")
    for twin_prime in twin_primes:
        print(twin_prime[0], twin_prime[1])


# Get user input for the range of numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Print all primes in the range
printPrimesInRange(start, end)

# Print all twin primes in the range
printTwinPrimesInRange(start, end)