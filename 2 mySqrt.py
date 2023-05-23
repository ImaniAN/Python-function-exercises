def mySqrt():
    # Request user input for the number
    n = float(input("Enter a number: "))
    
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    
    # Initial guess: n/2
    guess = n / 2.0
    
    while True:
        # Compute the new guess using the Newton's formula
        new_guess = 0.5 * (guess + (n / guess))
        
        # Check if the new guess is close enough to the previous guess
        if abs(new_guess - guess) < 1e-9:
            break  # Stop iteration if the guess is close enough
        
        # Update the guess with the new guess for the next iteration
        guess = new_guess
    
    return guess

# Call the function to approximate the square root
result = mySqrt()

# Print the result
print(f"The square root is approximately: {result}")
