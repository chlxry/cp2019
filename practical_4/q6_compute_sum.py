# Write a recursive function sum_digits(n) that computes the sum of the digits in an integer n: 

# For example, sum_digits(234) returns 9.

def sum_digits(n):
    sum = 0
    while (n > 0):
        dig = n % 10
        sum = sum + dig
        n = n // 10
    print(sum)
