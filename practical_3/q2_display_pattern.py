# Write a function display_pattern(n) to display a pattern as follows:
#               1
#             2 1
#           3 2 1
# ...
# n n-1 ... 3 2 1


n = int(input("enter 'n' here: "))

for row in range(n+1):
    print(" "*(n - row), end="")
    for col in range(row, 0, -1):
        print(col, end="")
    print()
