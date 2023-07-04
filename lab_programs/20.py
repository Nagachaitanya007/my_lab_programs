# Exception Handling Example
try:
    # Code that may raise an exception
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")



finally:
    print("Exception handling example completed.")
