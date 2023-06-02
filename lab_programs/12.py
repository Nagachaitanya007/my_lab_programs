# Take input from the user
word = input("Enter a word: ")

# Initialize counters for letters and vowels
letter_count = 0
vowel_count = 0

# Iterate over each character in the word
for char in word:
    # Check if the character is a letter
    if char.isalpha():
        letter_count += 1
        # Check if the letter is a vowel
        if char.lower() in "aeiou":
            vowel_count += 1

# Print the number of letters and vowels
print("Number of letters:", letter_count)
print("Number of vowels:", vowel_count)
