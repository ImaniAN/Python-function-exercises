def myPi():
    # Prompt the user to enter the number of terms to use in the series
    num_terms = int(input("Enter the number of terms to use in the series: "))
    
    # Initialize the variables for the series calculation
    pi_approximation = 0.0
    sign = 1.0
    
    # Iterate through each term in the series
    for i in range(num_terms):
        # Calculate the current term using the Madhava-Leibniz series formula
        term = sign / (2 * i + 1)
        
        # Add or subtract the term from the approximation based on the sign
        pi_approximation += term
        
        # Toggle the sign for the next term
        sign *= -1.0
    
    # Multiply the approximation by 4 to get the value of PI
    pi_approximation *= 4.0
    
    # Print the approximation of PI
    print("Approximation of PI:", pi_approximation)

# Call the myPi() function
myPi()
