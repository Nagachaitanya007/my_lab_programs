# Function to insert a number into a sorted array
def insert_into_sorted_array(array, num):
    # Find the index where the number should be inserted
    index = 0
    while index < len(array) and array[index] < num:
        index += 1
    
    # Insert the number at the found index
    array.insert(index, num)

# Take input from the user
n = int(input("Enter the number of elements in the array: "))
array = []

# Take n numbers as input and store them in the array (assuming the array is initially sorted)
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    array.append(num)

# Take the number to be inserted from the user
num_to_insert = int(input("Enter the number to be inserted: "))

# Insert the number into the sorted array
insert_into_sorted_array(array, num_to_insert)

# Print the updated array
print("Updated array:", array)
