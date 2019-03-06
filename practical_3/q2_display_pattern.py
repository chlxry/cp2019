# Write a function display_pattern(n) to display a pattern as follows:
#               1
#             2 1
#           3 2 1
# ...
# n n-1 ... 3 2 1


n = 9
j = n + 1

for i in range (j):
    while j > (j - i):
        if j > (j - i):
            print('{1:>{0}}'.format(j, i))
            i = i - 1
            j = j - 1
        else:
            break
