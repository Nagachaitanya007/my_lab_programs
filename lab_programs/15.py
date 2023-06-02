# Function for binary search
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Take input from the user
n = int(input("Enter the number of elements in the array: "))
array = []

# Take n numbers as input and store them in the array
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    array.append(num)

# Sort the array
array.sort()

# Take the element to be searched from the user
target = int(input("Enter the element to be searched: "))

# Perform binary search
index = binary_search(array, target)

# Print the result
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print("Element not found in the array.")
