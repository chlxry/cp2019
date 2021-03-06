# The greatest common divisor (GCD) of two positive integers m and n, gcd(m, n) can be defined recursively as follows: 

# If m % n is 0, gcd(m, n) is n.
# Otherwise, gcd(m, n) is gcd(n, m % n).

# Write a recursive function gcd(m, n) to find the GCD. Write a test program that computes gcd(24, 16) and gcd(255, 25).

def gcd(m, n): 
    if n == 0: 
        return m 
    else: 
        return gcd(n , m % n) 
      
# test program
gcd(24, 16) # input
8 # output

gcd(255, 25) # input
5 # output
