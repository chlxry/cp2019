# Write a program that prompts the user to enter the month and year, and displays the number of days in the month. 
# For example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. 
# If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days. 
x = int(input("enter month here: "))
y = int(input("enter year here: "))

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print(month[x-1] + " " + str(y) + " has 31 days")

elif x == 2 and y % 4 == 0: 
    print(month[x-1] + " " + str(y) + " has 29 days")
    
elif x == 2 and y % 4 == 1 or y % 4 == 2 or y % 4 == 3:
    print(month[x-1] + " " + str(y) + " has 28 days")

else:
    print(month[x-1] + " " + str(y) + " has 30 days")
