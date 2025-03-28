# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using ljust() function.

# Input string
string = input("Enter a sentence: ")

# Justify to the left without ljust()

def ljust_alternative(string, width=30):
    if len(string) >= width:
        return string
    # Prints _ to show left justified
    return string + '_' * (width - len(string))

print(ljust_alternative(string))