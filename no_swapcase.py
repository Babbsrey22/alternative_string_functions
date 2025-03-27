# Prog08. swapcase() reverse the casing of each of the character of the string. 
# Create a program that do the same functionality without using swapcase() function.

# Input string
string = input("Enter a sentence: ")

# Convert lowercase to uppercase and vice versa, without using swapcase()

def swapcase_alternate(s): 
    result = ''
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result
        
print(swapcase_alternate(string))