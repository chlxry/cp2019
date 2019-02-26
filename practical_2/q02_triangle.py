# Write a program that reads three edges for a triangle and determines whether the input is valid
# The input is valid if the sum of any two edges is greater than the third edge
# The program will compute the perimeter of the triangle if the input is valid
# Otherwise, display that the input is invalid. 2 sample sessions are as follows:

# Enter side 1: 2
# Enter side 2: 2
# Enter side 3: 1
# Perimeter = 5

# Enter side 1: 1
# Enter side 2: 2
# Enter side 3: 1
# Invalid triangle!

x = int(input("enter side 1: "))
y = int(input("enter side 2: "))
z = int(input("enter side 3: "))
sum = x + y + z

if (x + y) > z and (x + z) > y and (y + z) > x:
    print("perimeter: " + str(sum))

else:
    print("invalid triangle boiii")
