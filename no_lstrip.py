# Prog01. lstrip() remove the space characters at the beginning of the string. 
# Create a program that do the same functionality without using lstrip() function.

# Input string
string = input("Enter a sentence: ")

# Remove left spaces without lstrip()

def lstrip_alternative():
    spaces = 0

    while spaces < len(string):
        if string[spaces] == " ":
            spaces += 1
        else:
            break
    return string[spaces:]

print(lstrip_alternative())