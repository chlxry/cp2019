# Write a program q5_upper_to_lower.py that converts an uppercase letter from standard input to a lowercase letter 
# by making use of its ASCII value

# w/o making use of ASCII
upper = input("Input word with uppercase here boiii: ")
print("Word in lowercase: " + upper.lower())

# making use of ASCII
upper = input("Input uppercase letter here boiii: ")
print("Lowercase letter: " + chr(ord(upper) + 32))
