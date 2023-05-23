import math

def areaOfCircle():
    try:
        # Prompt the user to enter the radius of the circle
        radius = float(input("Enter the radius of the circle: "))
        
        # Check if the radius is negative
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid positive number.")
        return

    # Calculate the area of the circle using the formula: pi * radius^2
    area = math.pi * math.pow(radius, 2)
    return area

# Call the areaOfCircle function to calculate the area of the circle
circle_area = areaOfCircle()

# Check if the circle_area is not None (i.e., a valid area is calculated)
if circle_area is not None:
    # Print the calculated area of the circle
    print("Area of the circle:", circle_area)
