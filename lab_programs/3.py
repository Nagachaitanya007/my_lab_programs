import cmath

# Take input from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = (b**2) - (4*a*c)

# Find the solutions
solution1 = (-b + cmath.sqrt(discriminant)) / (2*a)
solution2 = (-b - cmath.sqrt(discriminant)) / (2*a)

# Print the solutions
print("The solutions are:")
print("x1 =", solution1)
print("x2 =", solution2)
