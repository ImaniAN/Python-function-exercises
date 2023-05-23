def gcd(m, n):
    # Check if either m or n is zero
    if m == 0:
        return n
    if n == 0:
        return m

    while n != 0:
        # Calculate the remainder
        remainder = m % n

        # Update m and n
        m = n
        n = remainder

    return m


def lcm(m, n):
    # Calculate the product of m and n
    product = m * n

    # Calculate the gcd of m and n
    gcd_val = gcd(m, n)

    # Calculate the lcm using the formula lcm(m, n) = (m * n) / gcd(m, n)
    lcm_val = product // gcd_val

    return lcm_val


# Get user input for m and n
m = int(input("Enter the first number (m): "))
n = int(input("Enter the second number (n): "))

# Calculate the gcd of m and n
gcd_val = gcd(m, n)
print("GCD of", m, "and", n, "is", gcd_val)

# Calculate the lcm of m and n
lcm_val = lcm(m, n)
print("LCM of", m, "and", n, "is", lcm_val)