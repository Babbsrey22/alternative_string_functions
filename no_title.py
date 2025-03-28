# Prog10. title() makes all first letter of each word in the string capital letter,and all other letter in small case. 
# Create a program that do the same functionality without using title() function.

# Input string
string = input("Enter a sentence: ")

# Convert all first letters of each word to uppercase without title()

def title_alternative():
    result = []
    word = string.split()

    for char in word:
        if len(char) > 0:
            result.append(char[0].upper() + char[1:].lower())
        else:
            result.append(char)
        
    return " ".join(result)

print(title_alternative())