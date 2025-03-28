# Prog09. capitalize() makes the first letter of the string capital letter, and all other letter in small case. 
# Create a program that do the same functionality without using capitalize() function.

# Input string
string = input("Enter a sentence: ")

# Convert only first letter of string to uppercase without capitalize()

def capitalize_alternate(s):
    result = ''
    for char in range(len(s)):
        if char == 0 and s[char].isalpha():
            result += s[char].upper()
        else:
            result += s[char]
    return result

print(capitalize_alternate(string))