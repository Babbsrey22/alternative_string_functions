# Prog04. isupper() check if all characters of the string is on upper case. 
# Create a program that do the same functionality without using isupper() function.

# Input string
string = input("Enter a sentence: ")

# Print 'True' if string is in uppercase without isupper()

def isupper_alternative(s):
    for char in s:
        if 'a' <= char <= 'z':
            return False
    return all('A' <= char <= 'Z' for char in s)

print("Are all characters in uppercase?", isupper_alternative(string))