# Initialize an empty stack
stack = []

# Function to push an element onto the stack
def push(element):
    stack.append(element)
    print("Element", element, "pushed onto the stack.")

# Function to pop an element from the stack
def pop():
    if len(stack) == 0:
        print("Stack is empty. Cannot perform pop operation.")
    else:
        element = stack.pop()
        print("Element", element, "popped from the stack.")

# Function to display the elements in the stack
def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Elements in the stack:", stack)

# Perform stack operations
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Quit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        element = input("Enter the element to be pushed: ")
        push(element)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
