number = int(input(" Enter the number to check whether its even or odd"))

if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(f"The number {number} is {result}.")
