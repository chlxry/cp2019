# A solution to find the greatest common divisor of two integers n1 and n2 is as follows: 
# First find d to be the minimum of n1 and n2, 
# then check whether d, d-1, … d-2, 2, or 1 is a divisor for both n1 and n2 in this order. 
# The first such common divisor is the greatest common divisor for n1 and n2. Write a program to implement this solution.

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
  
a = int(input("enter integer here: "))
b= int(input("enter integer here: "))
  
print ("the greatest common divisor of " + str(a) + " and " + str(b) + " is " + str(gcd(a, b))) 
