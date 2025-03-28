# Prog03. lower() converts all characters of the string into lower case. 
# Create a program that do the same functionality without using lower() function.

# Input string
string = input("Enter a sentence: ")

# Convert to lowercase without lower()

def lowercase_alternative(s):
    result = " "
    for char in s:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

print(lowercase_alternative(string))