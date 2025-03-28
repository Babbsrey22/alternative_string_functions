# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
# Create a program that do the same functionality without using removeprefix() function.

# Input string
string = input("Enter a sentence: ")

# Remove certain number of characters without removeprefix()

def removeprefix_alternative():
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string
    
prefix = input("What should this string NOT start with? Enter: ")
print(f"This string without the prefix '{prefix}' is:", "\n", removeprefix_alternative())