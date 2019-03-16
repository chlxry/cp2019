# Write a recursive function find_num_uppercase(str) to return the number of uppercase letters in a string str.

# For example, find_num_uppercase('Good MorninG!') returns 3.

def find_num_uppercase(string):
    upper = 0
    for i in string:
        if(i.isupper()):
            upper = upper + 1
    print(upper)
