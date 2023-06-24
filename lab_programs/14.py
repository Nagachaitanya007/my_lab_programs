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

''' def linear_search(list, element):
  for i in range(len(list)):
    if list[i] == element:
      return i
  return -1


def main():
  list = []
  n = int(input("Enter the number of elements in the list: "))
  for i in range(n):
    element = int(input("Enter element number {}: ".format(i + 1)))
    list.append(element)

  element = int(input("Enter the element to search for: "))
  index = linear_search(list, element)

  if index == -1:
    print("Element not found")
  else:
    print("Element found at index:", index)


if __name__ == "__main__":
  main()
 '''
