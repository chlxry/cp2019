# Write a program q1_fahrenheit_to_celsius.py that reads a Fahrenheit degree in double (floating point / decimal) from standard input
# then converts it to Celsius and displays the result in standard output
# The formula for the conversion is as follows: celsius = (5/9) * (fahrenheit - 32)

fahrenheit = float(input("Input the Fahrenheit degree here boiii: "))
celsius = (5/9) * (fahrenheit - 32)

print("degree in Celsius: " + "{0:.2f}".format(celsius))
