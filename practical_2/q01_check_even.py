# Write a program that reads an integer and checks whether it is even. 2 sample sessions are as follows:
# Enter number: 25
# 25 is odd
# Enter number: 8
# 8 is even

x = int(input("insert integer here: "))

if x % 2 == 0 :
    print(str(x) + " is even")
   
else:
    print(str(x) + " is odd")
