# Take input from the user
num1, num2 = float(input("Enter the first number: ")), float(input("Enter the second number: "))

print("Before swapping:")
print("First number =", num1)
print("Second number =", num2)

# Swapping logic
num1, num2 = num2, num1

print("After swapping:")
print("First number =", num1)
print("Second number =", num2)
