# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. 
# Create a program that do the same functionality without using center() function.

# Input string
string = input("Enter a sentence: ")

# Center align without using center()

def center_alternative(s):
    padding = 30
    left_padding = padding // 2
    right_padding = padding - left_padding

    return ' ' * left_padding + s + ' ' * right_padding

print(center_alternative(string))