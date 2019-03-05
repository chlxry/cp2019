# Write a program that reads an integer and displays all its smallest factors. 
# For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.

def factors(n):
    factors = []
    m = 2
    while n > 1 and m < n:
        for i in range (1,int(n)):
            if n % m == 0:
                factors.append(m)
                m = m
                n = n/m
            else:
                m = m + 1 
    print(factors)

input = int(input("Enter an integer: "))
factors(input)
