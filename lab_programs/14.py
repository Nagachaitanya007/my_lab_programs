# Take input from the user
n = int(input("Enter the number of elements in the array: "))
array = []

# Take n numbers as input and store them in the array
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    array.append(num)

# Take the element to be searched from the user
target = int(input("Enter the element to be searched: "))

# Perform linear search
found = False
index = -1

for i in range(n):
    if array[i] == target:
        found = True
        index = i
        break

# Print the result
if found:
    print(f"Element {target} found at index {index}.")
else:
    print("Element not found in the array.")
