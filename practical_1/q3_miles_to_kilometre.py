# Write a program q3_miles_to_kilometre.py that reads a number in miles, converts it to kilometres, and displays the result
# One mile is 1.60934 kilometres
# Display your answer correct to 3 decimal places.

miles = float(input("Input the number of miles here boiii: ")) 
kilometres = miles * 1.60934

print("Number of kilometres: " + "{0:.3f}".format(kilometres))
