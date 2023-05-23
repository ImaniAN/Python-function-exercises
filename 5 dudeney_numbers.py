def sumDigits(n):
    sum = 0  # Initialize the sum variable to 0
    while n > 0:  # Continue looping until n becomes 0
        digit = n % 10  # Get the rightmost digit of n
        sum += digit  # Add the digit to the sum
        n //= 10  # Remove the rightmost digit from n
    return sum  # Return the sum of the digits


def findDudeneyNumbers():
    dudeney_numbers = []  # Create an empty list to store Dudeney numbers
    for num in range(1, 20001):  # Iterate through numbers from 1 to 20000 (inclusive)
        digit_sum = sumDigits(num)  # Calculate the sum of digits for the current number
        if num == digit_sum ** 3:  # Check if the number is equal to the cube of its digit sum
            dudeney_numbers.append(num)  # Add the number to the list of Dudeney numbers
    return dudeney_numbers  # Return the list of Dudeney numbers

def printDudeneyNumbers():
    dudeney_nums = findDudeneyNumbers()  # Find all Dudeney numbers between 1 and 20000
    for num in dudeney_nums:  # Iterate through each Dudeney number
        digit_sum = sumDigits(num)  # Calculate the sum of digits for the current Dudeney number
        
        # Create the equation string in the format "number = digit_sum x digit_sum x digit_sum"
        equation = f"{num} = {digit_sum} x {digit_sum} x {digit_sum}"
        
        # Create the sum equation string in the format "digit_sum = digit1 + digit2 + ..."
        sum_equation = f"{digit_sum} = {' + '.join(str(digit) for digit in str(num))}"
        
        # Print the Dudeney number, the cube equation, and the sum equation
        print(f"{equation} and {sum_equation}")


# Print all Dudeney numbers between 1 and 20000 in the requested format
printDudeneyNumbers()

# Find and print all Dudeney numbers between 1 and 20000
dudeney_nums = findDudeneyNumbers()
print("Dudeney numbers between 1 and 20000:")
print(dudeney_nums)
