# Write a program that prompts the user to enter a year and determines whether it is a leap year
# A year is a leap year if it is divisible by 4 but not 100, or is divisible by 400. 

# Sample sessions:

# Enter year: 2012
# Leap

# Enter year: 2013
# Non-Leap

x = int(input("enter year here: "))

if x % 4 == 0:
    print("LEAPPPP")
else:
    print("non-leap :(")
