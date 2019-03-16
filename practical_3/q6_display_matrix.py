# Write a function print_matrix(n) that displays an n by n matrix, where n is a positive integer entered by the user. 
# Each element is 0 or 1, which is generated randomly. A 3 by 3 matrix may look like this:

# 0 1 0
# 0 0 0
# 1 1 1 

def print_matrix(n):
    import random
    n = int(input("enter 'n': "))
    for columns in range(n):
        for rows in range(n):
            print(random.randint(0, 1), end = " ")
        print()
