# Prog05. endswith() check if the string end part matches the function parameter. 
# Create a program that do the same functionality without using endswith() function.

# Input string
string = input("Enter a sentence: ")

# Print 'True' if string ends with a certain parameter without endswith()

def endswith_alternative(s, suffix):
    if len(suffix) <= len(s):
        result = s[-len(suffix):] == suffix
    else: 
        False
    return result

suffix = input("What should this string end with? Enter: ")
print(f"Does it end with '{suffix}'?", endswith_alternative(string, suffix))