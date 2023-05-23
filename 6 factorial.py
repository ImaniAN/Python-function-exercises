def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i  # Multiply the current number with the previous result
        return result

# Request user input for the number
number = int(input("Enter a number: "))

# Calculate the factorial using the factorial() function
result = factorial(number)

# Generate the expanded factorial notation
expanded_notation = " x ".join(str(i) for i in range(1, number + 1))

# Print the factorial of the number with expanded factorial notation
print(f"The factorial of {number} ({expanded_notation}) is: {result}")