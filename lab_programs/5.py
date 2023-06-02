# Celsius to Fahrenheit
celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = (celsius_temp * 9/5) + 32
print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees Fahrenheit.")

# Fahrenheit to Celsius
fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
celsius_temp = (fahrenheit_temp - 32) * 5/9
print(f"{fahrenheit_temp} degrees Fahrenheit is equal to {celsius_temp} degrees Celsius.")
