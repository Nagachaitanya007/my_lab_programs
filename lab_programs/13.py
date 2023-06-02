# Take input from the user
n = int(input("Enter the number of elements in the array: "))
array = []

# Take n numbers as input and store them in the array
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    array.append(num)

# Initialize sum variables for positive numbers and negative numbers
positive_sum = 0
negative_sum = 0

# Iterate over each element in the array
for num in array:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num

# Print the sum of positive numbers and negative numbers
print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)
