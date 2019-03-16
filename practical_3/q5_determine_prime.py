# Write a function to determine whether an integer is a prime number. 
# An integer greater than 1 is a prime number if its only divisor is 1 or itself. 
# For example, is_prime(11) returns True, and is_prime(9) returns False.

# Use the is_prime(n) function to find the first thousand prime numbers and display every ten prime numbers in a row, as follows:

# 2   3   5   7   11   13   17   19   23   29
# 31  37  41  43  47   53   59   61   67   71
# 73  79  83  89  97  ...
# ...

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False                
        else:
            return True
          
list = []
n = 2
rows = 0
while rows < 100:
    while len(list)<10:
        if is_prime(n) is True:
            list.append(n)
            n = n + 1
        else:
            n = n + 1
    print("{0:<5}".format(*list), "{1:<5}".format(*list), "{2:<5}".format(*list), "{3:<5}".format(*list), "{4:<5}".format(*list), "{5:<5}".format(*list), "{6:<5}".format(*list), "{7:<5}".format(*list), "{8:<5}".format(*list), "{9:<5}".format(*list), sep = " ")
    rows = rows + 1
    list = []
