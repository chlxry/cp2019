# Write a function gcd(m, n) that returns the greatest common divisor between two positive integers:

# Write a test program that computes gcd(24, 16) and gcd(255, 25).

def gcd(m, n): 
    if n == 0: 
        return m 
    else: 
        return gcd(n , m % n) 
  
m = int(input("enter integer here: "))
n = int(input("enter integer here: "))
  
print ("the greatest common divisor of " + str(m) + " and " + str(n) + " is " + str(gcd(m, n))) 
