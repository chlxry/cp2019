# Write a recursive function reverse_int(n) that reverses the digits of an integer n: 

# For example, reverse_int(12345) displays 54321.

def reverse_int(n):
    reverse = 0    
    while(n > 0):    
        reminder = n %10    
        reverse = (reverse *10) + reminder    
        n = n //10    
    print("reverse of entered number is = " + str(reverse))
