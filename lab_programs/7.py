# Take input from the user
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end+1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

#for single number given by user
'''num = int(input(" Enter the number :"))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"The number {num} is prime.")
else:
    print(f"The number {num} is not prime.")'''

#with def
'''def is_prime(number):
    if number <= 1:
        return False

    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

# Example usage
num = 17
if is_prime(num):
    print(f"The number {num} is prime.")
else:
    print(f"The number {num} is not prime.")'''
