# Write a function reverse_int(n) to display an integer in reverse order:

# For example, reverse_int(3456) displays 6543.

n = (input("enter integer here: "))
reverse = ""

for i in range(len(n), 0, -1):
    reverse += n[i-1]
print("integer in reversed order: " + str(reverse))
