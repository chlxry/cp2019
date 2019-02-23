# Write a program q4_sum_digits.py that reads an integer between 0 and 1000 and adds all the digits in the integer
# For example, if an integer is 932, the sum of all its digits is 14
# Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit
# For instance, 932 % 10 = 2 and 932 // 10 = 93 

x = int(input("Input a number here boiii: "))
sum = 0
while (x > 0):
    dig = x % 10
    sum = sum + dig
    x = x // 10
    
print("The sum of digits is: " + str(sum))
